from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from myapp.models import Author, Quote, Tag


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['author_name', 'date_of_birth',
                  'place_of_birth', 'author_description']


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['quote_name', 'author_name', 'tags']


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['tags_name']
