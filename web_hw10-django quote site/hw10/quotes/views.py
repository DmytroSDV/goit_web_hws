from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.core.paginator import Paginator
from django.db.models import Count

from .utils import get_mongodb
from .models import Author, Quote, Tag
from .forms import AuthorForm, QuoteForm,SearchForm

from utils.scrape_data import run_spider
from utils.migrate_from_scrape_files import fill_database

def main(request, page=1):

    quotes = Quote.objects.all()
    form = SearchForm()
    if 'search_tags' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            search_tags = form.cleaned_data['search_tags']
            quotes = quotes.filter(tags__name__icontains=search_tags)
    
    top_ten_tags = Tag.objects.annotate(num_quotes=Count('quote')).order_by('-num_quotes')[:10]
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, "quotes/index.html", context={'quotes': quotes_on_page, 'top_ten_tags': top_ten_tags, "form": form})

def author_about(request,fullname):
    author=Author.objects.get(fullname=fullname)
    return render(request,'quotes/author_about.html', context={'author': author})

def tag_info(request, name, page=1):
    quotes = Quote.objects.filter(tags__name=name)
    form = SearchForm()
    if 'search_tags' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            search_tags = form.cleaned_data['search_tags']
            quotes = quotes.filter(tags__name__icontains=search_tags)
    
    top_ten_tags = Tag.objects.annotate(num_quotes=Count('quote')).order_by('-num_quotes')[:10]
    per_page = 3
    paginator2 = Paginator(list(quotes), per_page)
    quotes_on_page = paginator2.page(page)
    return render(request, "quotes/taginfo.html", context={'quotes': quotes_on_page, 'top_ten_tags': top_ten_tags})

@login_required
def new_author(request):

    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.created_by = request.user.username
            author.save()
            return redirect(to='quotes:root')
        else:
            return render(request, 'quotes/new_author.html', {'form': form})

    return render(request, 'quotes/new_author.html', context={'form': AuthorForm()})

@login_required
def new_quote(request):

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.created_by = request.user.username
            quote.save()
            form.save_m2m()
            return redirect(to='quotes:root')
        else:
            return render(request, 'quotes/new_quote.html', {'form': form})

    return render(request, 'quotes/new_quote.html', context={'form': QuoteForm()})


def get_data(request):
    run_spider()
    fill_database()
    return redirect(to='quotes:root')