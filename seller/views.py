from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from costomer.models import state , city
from .models import seller_shop_details, products
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from  .models import seller_shop_details

 
 
def go_to_shop(request, id): 

    seller_product_id = products.objects.filter(shop_name_id = id)
    seller_id  = seller_shop_details.objects.get(id = id)
    seller_name  = seller_shop_details.objects.get(full_name = seller_id.full_name)

    params = {
        'seller_name' : seller_name,
        'seller_product_id' : seller_product_id,
        'user' : 'costomer'
    }
        
    return render(request, 'seller/seller_home_page.html', params)
 

def seller_logout(request):
    logout(request)
    return redirect('/')

def seller_login(request):

    if request.method == "POST":

        username  = request.POST['login_username']
        password = request.POST['login_password']

        user = authenticate(username = username , password = password)

        if user is not None:

            confirm_seller = seller_shop_details.objects.filter(full_name = username)

            if len(confirm_seller) !=0:

                login(request , user)
  
                seller_name = seller_shop_details.objects.get(full_name__iexact = username)
                seller_product_id = products.objects.filter(shop_name_id = seller_name.id)


                params = {
                    'seller_name' : seller_name,
                    'seller_product_id' :seller_product_id,
                    'user' : 'seller'
                }

                return render(request, 'seller/seller_home_page.html',params)

            else:
                return HttpResponse("you are not a seller my boy")
        else:
            return HttpResponse("not a seller")
    

def home_page(request,id): 
    if id==0:
        id 
    if request.method =="POST":
        product_name = request.POST['product_name']
        product_price = request.POST['product_price']
        product_description = request.POST['product_description']
        shop_name = request.POST['shop_name']
        product_image = request.FILES.get('product_image')

        print(product_image)

        seller_name  = seller_shop_details.objects.get(full_name = shop_name)

        ins = products(product_name = product_name , product_price = product_price, 
                        product_description = product_description,
                        shop_name_id = seller_name.id , product_image = product_image)
        ins.save()

        seller_product_id = products.objects.filter(shop_name_id = seller_name.id)



        params = {
            'seller_name' : seller_name,
            'seller_product_id' : seller_product_id,
            'id' : id
        }

        return render(request, 'seller/seller_home_page.html',params)
    else:

        seller_product_id = products.objects.filter(shop_name_id = id)
        params = {
            #'seller_name' : seller_name,
            'seller_product_id' : seller_product_id,
            'id' : id
        }
        return render(request, 'seller/seller_home_page.html',params)

def registration_page(request):

    if request.method == "POST":
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        states = request.POST['input_state']
        citys = request.POST['input_city']
        zip_code = request.POST['input_zip']
        shop_address = request.POST['shop_address']
        shop_cat = request.POST['shop_cat']
        seller_image = request.FILES.get('seller_image') 
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        shop_description = request.POST['shop_description']


        state_id = state.objects.get(state_name = states)
        city_id = city.objects.get(city_name = citys)

        myuser = User.objects.create_user(full_name, email, password)
        myuser.save() 

        ins = seller_shop_details(full_name = full_name , email = email , phone_number = phone_number , state = state_id, city = city_id,
                                 zip_code = zip_code, shop_address = shop_address , shop_category = shop_cat ,
                                 password = password , confirm_password = confirm_password , shop_description = shop_description,
                                  seller_image = seller_image)
        ins.save()

        
       
        return HttpResponse("congo reg compelete")



    states = state.objects.all()
    cities = city.objects.all()
    params = {
        'all_state' : states,
        'all_city' : cities
    }
    return render(request, 'seller/seller_registration_page.html', params)

def order_page(request):
    return render(request, 'seller/seller_order_page.html')

def contact_seller(request):
    return render(request, 'seller/seller_contact_page.html')

def add_items(request):

    return render(request,'seller/add_items.html')
  