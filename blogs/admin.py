from django.contrib import admin

# Register your models here.


class User(admin.ModelAdmin):
    list_display = ["id", "fullname", "email"]