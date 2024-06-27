from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import Author, Quote, Tag
from .forms import AuthorForm, QuoteForm, UserRegisterForm, TagForm
from django.contrib.auth.decorators import login_required
from bs4 import BeautifulSoup
import requests


def homepage(request):
    return render(request, 'myapp/homepage.html')


def register(request):
    register_form = UserRegisterForm(request.POST or None)
    if register_form.is_valid():
        try:
            register_form.save()
            username = register_form.cleaned_data.get('username')
            password_1 = register_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password_1)
            login(request, user)
            return redirect('login')
        except Exception:
            return redirect('login')
    return render(request, 'myapp/register.html', {'register_form': register_form})


def logout_view(request):
    logout(request)
    return redirect('homepage')


def authors(request):
    all_authors = Author.objects.all()
    return render(request, 'myapp/authors.html', {'Allauthors': all_authors})


def quotations(request):
    all_quotes = Quote.objects.all()
    return render(request, 'myapp/quotations.html', {'allquotes': all_quotes})


def authors_biography(request, author_name):
    author = Author.objects.all()
    return render(request, 'myapp/authorpage.html', {'author_name': author_name, 'author': author})


def add_author(request):
    author_form = AuthorForm(request.POST or None)
    if author_form.is_valid():
        author_form.save()
        return redirect(authors)
    return render(request, 'myapp/add_author.html', {'author_form': author_form})


def add_quote(request):
    quote_form = QuoteForm(request.POST or None)
    if quote_form.is_valid():
        quote_form.save()
        return redirect(quotations)
    return render(request, 'myapp/add_quote.html', {'quote_form': quote_form})


def add_tag(request):
    tag_form = TagForm(request.POST or None)
    if tag_form.is_valid():
        tag_form.save()
        return redirect(add_quote)
    return render(request, 'myapp/add_tag.html', {'tag_form': tag_form})


@login_required
def scrape(request):
    url = "http://quotes.toscrape.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')
    for quote in quotes:

        quote_name = quote.find('span', class_='text').get_text()
        author_name = quote.find('small', class_='author').get_text()
        tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]

        author_name, created = Author.objects.get_or_create(
            author_name=author_name)
        quote_obj, created = Quote.objects.get_or_create(
            quote_name=quote_name, author_name=author_name)

        for tag_name in tags:
            tag, created = Tag.objects.get_or_create(tags_name=tag_name)
            quote_obj.tags.add(tag)
    return redirect('login')
