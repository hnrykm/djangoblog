from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from blog.models import Post

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = "__all__"
    list_display = (
        "title",
        "slug",
        "status",
        "created_on"
    )
    list_filter = ("status",)
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)

