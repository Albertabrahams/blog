from post.api.serializers import PostSerializer, PostCreateSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView, RetrieveUpdateAPIView
from post.models import Post
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny
from post.api.permissions import IsOwner
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import CreateModelMixin

class PostListAPIView(ListAPIView, CreateModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content']

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'

class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'

class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwner]

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)

class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]

    # def perform_create(self, serializer):
    #     user = self.request.user
    #     serializer.save(user=user)

    #     # Mail gönderme işlemleri
    #     subject = "Yeni bir post oluşturuldu"
    #     message = "Hesabunız hacklendi. Şu hesaba para gönderin:))"
    #     recipient_list = ["halilibrahim.soyman@gmail.com"]
    #     send_mail(subject, message, from_email=None, recipient_list=recipient_list, fail_silently=False)

    #     return Response({"message": "Post başarıyla oluşturuldu ve e-posta gönderildi."})