from django import forms
from apps.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "text"]
