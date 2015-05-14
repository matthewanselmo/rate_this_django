from django import forms
from .models import Post, Comment, Tag


class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())

    class Meta:
        model = Post
        fields = ['title', 'description', 'image', 'tags']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']
