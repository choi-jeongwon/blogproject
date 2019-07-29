from django import forms
from .models import Blog

class NewPost(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body']