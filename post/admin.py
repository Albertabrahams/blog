from django.contrib import admin
from post.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug',  'user', 'modified']
    list_display_links = ['title']
    search_fields = ['title', 'content']
