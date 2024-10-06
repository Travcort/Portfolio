from django.conf import settings
from django.http import JsonResponse
from django.contrib.admin.views.decorators import staff_member_required
from .models import Post
from django.views import generic

@staff_member_required
def getTinyKey(request):
    if request.method == 'GET':
        return JsonResponse({'tiny_key': settings.TINY_KEY})
    else:
        return JsonResponse({'Error': 'Invalid Request Method'}, status=400)


class BlogListView(generic.ListView):
    queryset = Post.objects.filter(status='published').order_by('-created_on')
    template_name = 'blog/Landing.html'
    context_object_name = "Posts"


class BlogDetailedView(generic.DetailView):
    model = Post
    template_name = 'blog/Post.html'
    context_object_name = "post"