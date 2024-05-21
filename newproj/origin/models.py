from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class OriginPost(models.Model):
    name = models.CharField(max_length=100, blank=False)
    image = models.ImageField(upload_to='images/', blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image_alt = models.CharField(max_length=300, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post_type = (
        ('post', 'Post'),
        ('reels', 'Reels')
    )
    post_type = models.CharField(max_length=5, choices=post_type, blank=True)
    def __str__(self): 
        return self.name