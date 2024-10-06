from django.contrib import admin
from django.utils import timezone
from django import forms
from .models import Post

class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'content': forms.Textarea(attrs={'id': 'id_content'})
        }

def publish_posts(modeladmin, request, queryset):
    queryset.update(status='published', published_at=timezone.now())

publish_posts.short_description = 'Publish selected posts'

class AdminPost(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('title', 'category', 'author', 'created_on', 'published_at')
    list_filter = ('created_on', 'status', 'category')
    search_fields = ('title', 'content')
    actions = [publish_posts]

    class Media:
        js = (
            'js/tiny-mce.js',
        )


admin.site.register(Post, AdminPost)
