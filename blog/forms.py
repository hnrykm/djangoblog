from django.forms import ModelForm
from blog.models import Post


class NewPostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "author",
            "content",
            "status",
        ]
