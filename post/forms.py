from django import forms
from post.models import Post


class newPostForm(forms.ModelForm):
    Picture = forms.ImageField(required=True)
    Caption = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "django-input", "placeholder": "Caption"}
        ),
        required=True,
    )
    tag = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "django-input",
                "placeholder": "Tags - Seperate tags with Hash",
            }
        ),
        required=True,
    )

    class Meta:
        model = Post
        fields = ["Picture", "Caption", "tag"]
