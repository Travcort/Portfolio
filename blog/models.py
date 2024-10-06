from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class Post(models.Model):

    status_state = [
        ('draft', 'Draft'),
        ('published', 'Published')
    ]

    title = models.CharField(max_length=200, unique=True)
    category = models.CharField(max_length=20)
    thumbnail_text = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=status_state, default='draft')
    published_at = models.DateTimeField(blank=True, null=True)
    content = models.TextField()
    # When I become rich😭 image = models.ImageField(upload_to='post_images/', blank=True, null=True)

    def save(self, *args, **kwargs):
        # Automatically generate slug from title if it doesn't already exist
        if not self.slug:
            self.slug = slugify(self.title)  # Convert title to slug
        super().save(*args, **kwargs)  # Call the original save() method

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title
