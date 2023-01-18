from django.contrib import admin
from blog.models import Post, Tag, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ("likes",)


@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ("post", "author")
    list_display = ('post', 'author', 'published_at')


admin.site.register(Tag)
