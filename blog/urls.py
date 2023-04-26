from blog import views
from django.urls import path
from blog.views import posts_list, post_details

urlpatterns = [
    path("", posts_list, name="home"),
    path("<slug:slug>/", post_details, name="post_detail"),
    path("new_post/", views.NewPost.as_view(), name="new_post"),
]
