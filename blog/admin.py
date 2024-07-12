from django.contrib import admin
from django import forms
from .models import Post

class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'content': forms.Textarea(attrs={'id': 'id_content'})
        }

class AdminPost(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('title', 'slug', 'author', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('title', 'content')

    class Media:
        js = (
            'js/tiny-mce.js',
        )


admin.site.register(Post, AdminPost)
