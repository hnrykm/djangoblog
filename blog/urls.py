from django.urls import path
from blog.views import posts_list, post_details, new_post, edit_post, delete_post

urlpatterns = [
    path("", posts_list, name="home"),
    path("<slug:slug>/edit/", edit_post, name="edit_post"),
    path("<slug:slug>/delete_post/", delete_post, name="delete_post"),
    path("new_post/", new_post, name="new_post"),
    path("<slug:slug>/", post_details, name="post_detail")
    
]
