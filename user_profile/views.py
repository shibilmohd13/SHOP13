from django.shortcuts import render, redirect
from userlogin.models import *
from django.contrib import messages
from django.contrib.auth import authenticate

# Create your views here.

def profile(request):
    print(request.user)
    email = request.session['email']
    user = CustomUser.objects.get(email=email)
    user_data = Address.objects.filter(user=user)
    return render(request, 'user_profile/profile.html',{'user_data' : user_data})

def update_profile(request):
    if request.method == 'POST':
        email = request.session['email']
        user = CustomUser.objects.get(email=email)
        new_phone = request.POST.get('phone')
        if CustomUser.objects.exclude(id=user.id).filter(phone=new_phone).exists():
            messages.error(request, "phone number already exist in the database")
            print("already there")
            return redirect('user_profile')
        
        user.fullname = request.POST.get('fullname', user.fullname)
        user.phone = request.POST.get('phone', user.phone)
        user.save()
        primary_address_id  = request.POST.get('primary_address')
        Address

        
        messages.success(request, "updated successfully")

    return redirect('profile')

def change_password(request):
    if request.method == 'POST':
        email = request.session['email']
        user = CustomUser.objects.get(email=email)

        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        new_password_confirm = request.POST.get('password_confirm')
        
        new_user = authenticate(username=email, password=current_password)
        
        if user == new_user:
            if new_password == new_password_confirm:
                user.set_password(new_password)
                user.save()
                print('Profile changed') 
                return redirect('profile')
            else:
                print('Pass not match')
                return redirect('profile')
        else:
            print("not the current user")
            return redirect('profile')

def add_address(request):
    email = request.session['email']
    user = CustomUser.objects.get(email=email)
    
    name = request.POST['name']
    phone = request.POST['phone']
    street_address = request.POST['street_address']
    city = request.POST['city']
    state = request.POST['state']
    pincode = request.POST['pincode']

    new_address = Address(
        user = user,
        name = name,
        phone = phone,
        street_address = street_address,
        city = city,
        state = state,
        pin_code = pincode
    )
    new_address.save()
                
    return redirect('profile')

def edit_address(request, id):
    address = Address.objects.get(id=id)

    name = request.POST.get('name')
    phone = request.POST.get('phone')
    street_address = request.POST.get('street_address')
    city = request.POST.get('city')
    state = request.POST.get('state')
    pincode = request.POST.get('pincode')

    address.name = name
    address.phone = phone
    address.street_address = street_address
    address.city = city
    address.state = state
    address.pin_code = pincode

    address.save()

    return redirect('profile')

def delete_address(request, id):
    address = Address.objects.get(id=id)
    address.delete()
    return redirect('profile')