from rest_framework.serializers import ModelSerializer, SerializerMethodField
from comment.models import Comment
from rest_framework import serializers
from django.contrib.auth.models import User

class CommentCreateSerializer(ModelSerializer):

    class Meta:
        model = Comment
        exclude = ['created',]

    def validate(self, attrs):
        if attrs['parent']:
            if attrs['parent'].post != attrs['post']:
                raise serializers.ValidationError('Something went wrong')
        return attrs

class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'id']


class CommentListSerializer(ModelSerializer):

    replies = SerializerMethodField()
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
    
    def get_replies(self, obj):
        if obj.any_children:
            return CommentListSerializer(obj.children(), many=True).data
        return None

class CommentDeleteUpdateSerializer(ModelSerializer):
    
        class Meta:
            model = Comment
            fields = ['content',]

