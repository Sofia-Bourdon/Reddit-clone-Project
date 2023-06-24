from django.contrib import admin
from .models import Post, Comment, Subreddit
from django_summernote.admin import SummernoteModelAdmin
from django.db import models


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'subreddit', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('get_post_title', 'created_on', 'body')
    list_filter = ('created_on', 'approved')
    search_fields = ('name', 'email', 'post__title', 'body')
    fieldsets = (
        (None, {'fields': ('name', 'email', 'body')}),
        ('Status', {'fields': ('status',)}),
        ('Metadata', {'fields': ('post', 'created_on')}),
    )
    actions = [
        'approve_comments',
        'edit_comments',
        'delete_comments',
    ]
    
    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

    def get_post_title(self, obj):
        return obj.post.title

    get_post_title.short_description = 'Post Title'


admin.site.register(Subreddit)

