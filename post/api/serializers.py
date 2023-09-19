from post.models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='post:detail',
        lookup_field='slug'
    )

    class Meta:
        model = Post
        fields = [
            'user',
            'title', 
            'content',
            'created',
            'slug',
            'image',
            'url',
            'modified_by',
        ]

class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'title', 
            'content',
        ]