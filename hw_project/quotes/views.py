from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
# from .utils import get_mongodb

from .models import Tag, Autor, Quote
from .forms import AutorForm, QuoteForm


def main(request, page=1):
    # db = get_mongodb()
    quotes = Quote.objects.all()
    # quotes = db.quote.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})


def add_autor(request):
    if request.method == 'POST':
        autor_form = AutorForm(request.POST)
        if autor_form.is_valid():
            autor_form.save()
            return redirect('/')
    else:
        autor_form = AutorForm()

    return render(request, 'quotes/add_author.html', {'autor_form': autor_form})


def add_quote(request):
    if request.method == 'POST':
        quote_form = QuoteForm(request.POST)
        if quote_form.is_valid():
            quote_form.save()
            return redirect('/')
    else:
        quote_form = QuoteForm()

    return render(request, 'quotes/add_quote.html', {'quote_form': quote_form})


def detail(request, author_id):
    author = get_object_or_404(Autor, pk=author_id)
    return render(request, 'quotes/author.html', {'author': author})

