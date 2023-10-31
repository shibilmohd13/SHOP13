from products.models import *
from userlogin.models import *
def navbar_elements(request):
    categories_nav = Category.objects.exclude(is_listed=False)
    brands_nav = Brand.objects.exclude(is_listed=False)    
    try: 
        user = request.session['email']
        user_obj = CustomUser.objects.filter(email=user).first()
        return {'users' : user, 'categories_nav' : categories_nav , 'brands_nav' :brands_nav, 'user_obj' : user_obj}
    except:
        return {'users' : 'Login Now', 'categories_nav' : categories_nav , 'brands_nav' :brands_nav}
