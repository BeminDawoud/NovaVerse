from django import forms
from post.models import Post


class newPostForm(forms.ModelForm):
    picture = forms.ImageField(required=True)
    caption = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "django-input", "placeholder": "Caption"}
        ),
        required=True,
    )
    tags = forms.CharField(
        widget=forms.TextInput(attrs={"class": "django-input", "placeholder": "Tag"}),
        required=True,
    )

    class Meta:
        model = Post
        fields = ["picture", "caption", "tags"]
