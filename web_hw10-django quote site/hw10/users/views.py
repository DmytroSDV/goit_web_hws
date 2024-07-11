from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import RegisterForm, LoginForm, ProfileForm, QuoteForm

from quotes.models import Quote, Author, Tag

@login_required
def profile(request):
    quotes = Quote.objects.all()
    quotes_user = Quote.objects.filter(created_by=request.user)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users:profile')

    profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'users/profile.html', {'profile_form': profile_form, "quotes": quotes, "quotes_user": quotes_user})

@login_required
def logoutuser(request):
    logout(request)
    return redirect(to='quotes:root')

def signupuser(request):
    if request.user.is_authenticated:
        return redirect(to='quotes:root')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:root')
        else:
            return render(request, 'users/signup.html', context={"form": form})

    return render(request, 'users/signup.html', context={"form": RegisterForm()})


def loginuser(request):
    if request.user.is_authenticated:
        return redirect(to='quotes:root')

    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(request, 'Username or password didn\'t match')
            return redirect(to='users:login')

        login(request, user)
        return redirect(to='quotes:root')

    return render(request, 'users/login.html', context={"form": LoginForm()})

@login_required
def edit_quote(request, pk):
    quote = get_object_or_404(Quote, pk=pk)
    if request.method == 'POST':
        form = QuoteForm(request.POST, instance=quote)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    else:
        form = QuoteForm(instance=quote)
    return render(request, 'users/edit_quote.html', {'form': form})

@login_required
def delete_quote(request, pk):
    quote = get_object_or_404(Quote, pk=pk)
    if request.method == 'POST':
        quote.delete()
        messages.success(request, 'Quote deleted successfully')
        return redirect('users:profile')
    return render(request, 'users/delete_quote.html', {'quote': quote})


