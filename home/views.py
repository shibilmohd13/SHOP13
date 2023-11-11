from unicodedata import category
from django.shortcuts import render,redirect
from products.models import *
from userlogin.models import CustomUser
import smtplib
from . models import Contact
from django.contrib.auth import logout
from django.http import JsonResponse
from django.db.models import Q

# Create your views here.


# View to show the Home page of the Website ( Landing page )
def home(request):
    obj = Product.objects.prefetch_related('colorvarient_set__productimage_set').filter(is_listed=True).order_by('id')
    return render(request, 'home/home.html', {'obj': obj})


# View to show products in Shop
def shop(request):
    obj = Product.objects.prefetch_related('colorvarient_set__productimage_set').filter(is_listed=True).order_by('id')
    return render(request, 'home/shop.html', {'obj': obj })


# View to show the detailed Product detail of each product
def product_details(request,id):
    obj = ColorVarient.objects.prefetch_related('productimage_set').get(id=id)
    all_variants = ColorVarient.objects.filter(product=obj.product).prefetch_related('productimage_set').filter(is_listed=True).order_by("color")
    return render(request, 'home/details.html', {'item': obj, 'all_varients': all_variants })


# View for Provide the details of each color varient On clicking the images in the product details page
def get_color_variant_details(request, id):
    try:
        color_variant = ColorVarient.objects.get(id=id)
        image_urls = [img.image.url for img in color_variant.productimage_set.all()] # Get image URLs
        image_urls.reverse()
        data = {
            'discounted_price': color_variant.discounted_price,
            'price': color_variant.price,
            'color': color_variant.color,
            'quantity': color_variant.quantity,
            'id': color_variant.id,
            'image_urls': image_urls # Get image URLs
        }
        return JsonResponse(data)
    except ColorVarient.DoesNotExist:
        return JsonResponse({'error': 'ColorVariant not found'}, status=404)


# View for Logout the User
def logout_view(request):
    request.session.flush()
    return redirect('home')


# View for About section in website 
def about(request):
    return render(request, 'home/about.html')


# View for Contact section in website
# also provide a form for sending message to the Admin
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



# View for searching the products in the shop
# Searching through Products name, Category name and Brand name
def search(request):
    search_query = request.GET.get('search', '')  # Get the search query from the request

    name_query = Q(name__icontains=search_query)
    category_query = Q(category__name__icontains=search_query)
    brand_query = Q(brands__name__icontains=search_query)

    # Combine the three Q objects using the OR operator (|)
    combined_query = name_query | category_query | brand_query

    # Use the combined query to filter the Product objects
    products_match = Product.objects.filter(
        combined_query, is_listed=True
    )
    print(products_match)
    return render(request, "home/shop.html", {'obj': products_match})


