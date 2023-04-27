from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from django.contrib.auth.decorators import login_required
from blog.forms import NewPostForm, CommentForm

def posts_list(request):
    post_list = Post.objects.all()
    context = {
        "post_list": post_list,
    }
    return render(request, "index.html", context)

def post_details(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {
        "post": post,
        "object": post,
        "comments": comments,
        "new_comment": new_comment,
        "comment_form": comment_form
    }
    return render(request, "post_detail.html", context)

@login_required
def new_post(request):
    if request.method == "POST":
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = form.save(False)
            post.author = request.user
            post.save()
            return redirect("home")
    else:
        form = NewPostForm()
    context = {
        "form": form,
    }
    return render(request, "new_post.html", context)

@login_required
def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = NewPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("post_detail", slug=slug)
    else:
        form = NewPostForm(instance=post)
    context = {
        "post": post,
        "form": form,
    }
    return render(request, "edit_post.html", context)

@login_required
def delete_post(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == "POST":
        post.delete()
        return redirect("home")
    return render(request, "delete_post.html")
