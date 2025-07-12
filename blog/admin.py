from django.contrib import admin
from blog.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "views_counter")
    list_filter = ("name",)
    search_fields = ("name", "created_at", "views_counter")