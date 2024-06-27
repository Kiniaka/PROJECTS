from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('homepage/', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('add_tag/', views.add_tag, name='add_tag'),
    path('authors/', views.authors, name='authors'),
    path('quotations/', views.quotations, name='quotations'),
    path('authors/<str:author_name>/',
         views.authors_biography, name='authorpage'),
    path('scrape/', views.scrape, name = 'scrape')
]
