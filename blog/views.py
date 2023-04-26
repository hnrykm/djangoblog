from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from django.contrib.auth.decorators import login_required
from blog.forms import NewPostForm 

def posts_list(request):
    post_list = Post.objects.all()
    context = {
        "post_list": post_list,
    }
    return render(request, "index.html", context)

def post_details(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        "post": post,
        "object": post,
    }
    return render(request, "post_detail.html", context)

# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = "post_detail.html"

class NewPost(generic.CreateView):
    model = Post
    fields = [
        "title",
        "author",
        "content",
        "status",
    ]
    template_name = "new_post.html"

    