from django import forms
from .models import Comment, Post

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'comment')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'img', 'description', 'author')
