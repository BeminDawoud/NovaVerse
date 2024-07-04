from userauth.models import Profile
from django import forms


class EditProfileForm(forms.ModelForm):
    picture = forms.ImageField(required=True)
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "input-group"}), required=True
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "input-group"}), required=True
    )
    location = forms.CharField(
        widget=forms.TextInput(attrs={"class": "input-group"}), required=True
    )
    bio = forms.CharField(
        widget=forms.TextInput(attrs={"class": "input-group"}), required=True
    )

    class Meta:
        model = Profile
        fields = ["picture", "first_name", "last_name", "location", "bio"]
