from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from blog.models import Post, Comment

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

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "body",
        "post",
        "created_on",
        "active"
    )
    list_filter = (
        "active",
        "created_on"
    )
    search_fields = [
        "name",
        "email",
        "body"
    ]
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(active=True)