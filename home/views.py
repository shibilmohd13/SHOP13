from django.shortcuts import render,redirect
from products.models import *
from userlogin.models import CustomUser
import smtplib
from . models import Contact
from django.contrib.auth import logout

# Create your views here.
def home(request):
    obj = Product.objects.exclude(is_listed=False)[:8]
    return render(request, 'home/home.html', {'obj': obj})

def shop(request):
    obj = Product.objects.exclude(is_listed=False)
    clr = Color.objects.exclude(is_listed=False)
    return render(request, 'home/shop.html', {'obj': obj , 'colors_nav': clr})

def product_details(request,id):
    obj = Product.objects.filter(id=id)[0]
    return render(request, 'home/details.html', {'item': obj})

def logout_view(request):
    logout(request)
    return redirect('home')

def about(request):
    return render(request, 'home/about.html')


def contact(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        email = request.POST['email']
        user_message = request.POST['message']
        Contact.objects.create(first_name=first_name, last_name=last_name, phone=phone, email=email, message=user_message)
        return redirect("contact")
    return render(request, 'home/contact.html')

def search(request):
    search_query = request.GET['search']
    products_match = Product.objects.filter(name__icontains=search_query,is_listed=True)
    return render(request, "home/shop.html" , {'obj': products_match})


def profile(request):
    # request.session['users']
    # CustomUser.objects.filter(email=email)
    return render(request, 'home/profile.html')