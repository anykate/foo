from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('post', 'user', 'body')
        widgets = {
            'post': forms.HiddenInput(),
            'user': forms.HiddenInput()
        }
