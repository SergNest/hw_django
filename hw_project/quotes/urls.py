
from django.urls import path, include

from . import views


app_name = 'quotes'

urlpatterns = [
    path('add_author/', views.add_autor, name='add_author'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('', views.main, name='root'),
    path('users/', include('users.urls')),
    path('<int:page>', views.main, name='root_paginate'),
    path('author/<int:author_id>/', views.detail, name='author')
]
