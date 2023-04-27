from django.forms import ModelForm
from blog.models import Post
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