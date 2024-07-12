from django.shortcuts import render
from .models import Post
from django.views import generic


class BlogListView(generic.ListView):
    queryset = Post.objects.order_by('-created_on')
    template_name = 'blog-landing.html'
    context_object_name = "Posts"


class BlogDetailedView(generic.DetailView):
    model = Post
    template_name = 'detailed-post.html'
    context_object_name = "post"