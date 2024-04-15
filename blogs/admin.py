from django.contrib import admin
from .models import Article

# Register your models here.


class User(admin.ModelAdmin):
    list_display = ["id", "fullname", "email"]

class ArticleAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "publication_date", "image", "added_by"]

admin.site.register(Article, ArticleAdmin)
