from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    # When I become rich😭 image = models.ImageField(upload_to='post_images/', blank=True, null=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title
