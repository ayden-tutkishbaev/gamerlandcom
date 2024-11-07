from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
# from market.models import
from django.utils.translation import gettext_lazy as _

from blog.models import *


class CommentForm(forms.ModelForm):
    RATING = (
        ('five', _('5')),
        ('four', _('4')),
        ('three', _('3')),
        ('two', _('2')),
        ('one', _('1')),
        ('zero', _('0'))
    )

    class Meta:
        model = Comment
        fields = (
            'text',
            'rating'
        )

    widgets = {
        'text': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your comment'
        }),
        'author': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your name'
        }),
    }