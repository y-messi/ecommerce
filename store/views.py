from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms


# Create your views here.

def category(request, foo):
    # replace hyphens with spaces
    foo = foo.replace('-', '')
    # grab the category from the url
    
    try:
        #look up the category
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products':products, 'category':category})
    except:
        messages.success(request, ("That Category Doesnot Exist........."))
        return redirect('index')


def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product':product})
    
    
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products':products})

def about(request):
    return render(request, 'about.html', {})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been logged in successfully........"))
            return redirect('index')
        else:
            messages.success(request, ("There was an error, Try again ....."))
            return redirect('login')
    
    
    return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out..... Thanks for spending some time with us"))
    return redirect('login')


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # login user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("You have been Registered successfully!!!!!..... Welcome"))
            return redirect('login')
        else:
            messages.success(request, ("Whooops, there was a problem in registering..... Please try again"))
            return redirect('register')
    else:    
        return render(request, 'register.html', {'form':form})

    



