from django.forms import ModelForm
from blog.models import Post, Comment
from django_summernote.widgets import SummernoteWidget

class NewPostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "status",
        ]
        widgets = {
            "content": SummernoteWidget(),
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = (
            "name",
            "email",
            "body"
        )