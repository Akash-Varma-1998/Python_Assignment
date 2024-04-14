from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    publication_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='article_images/', blank=True, null=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self) :
        return str(self.title)
