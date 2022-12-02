from django.core.checks import messages
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from seller.models import seller_shop_details, products
from .models import customer, order
from .models import state , city , order
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
 

def place_order(request):
    if request.method == "POST":
        
        product_name = request.POST['product_name']
        shop_name = request.POST['shop_name']
        product_description = request.POST['product_description']
        user_name = request.POST['user_name']
        user_phone_number = request.POST['user_phone_number']
        delivery_address = request.POST['delivery_address']

        print(product_name, shop_name , product_description , user_name , user_phone_number , delivery_address)

        ins = order(delivery_address = delivery_address , costomer_name = user_name,
                    costomer_phone_number = user_phone_number, seller_name = shop_name,
                    )
        ins.save()

        return redirect('/')

def var():
    return -1

def buy_orders(request, id):

    if request.method == "POST":
        product = products.objects.get(id = id)
        
        userid = var()

        if userid != -1:
            costomer_data = customer.objects.get(full_name = userid)
            print(costomer_data)
            params={
            'product' : product,
            'costomer_data' : costomer_data
            }
            return render(request, 'buy_orders.html', params)
        else:
            return HttpResponse("please login")

        



def show_shop(request):

    input_city  = request.GET.get('input_city')
    input_category  = request.GET.get('input_category')
    all_state = state.objects.all()
    

    if input_category == 'select shop category':
        all_shop = seller_shop_details.objects.all()
     
    if input_category == 'Grocery':
        all_shop = seller_shop_details.objects.filter(shop_category = 'Grocery')
    
    if input_category == 'Cloth':
        all_shop = seller_shop_details.objects.filter(shop_category = 'clothes')
    
    if input_category == 'Stationery':
        all_shop = seller_shop_details.objects.filter(shop_category = 'Stationery')

    if input_category == 'Bakery':
        all_shop = seller_shop_details.objects.filter(shop_category = 'Bakery')

    params = {
        'all_shops':all_shop,
        'all_state' : all_state
    }
    
    return render(request,'shop_list_layout.html', params)


def input_state(request):
    
    input_state  = request.GET.get('input_state')
    all_state = state.objects.all()
    states = state.objects.get(state_name = input_state)
    all_city = city.objects.filter(state_id_id = states.id)
    all_shop = seller_shop_details.objects.filter(state_id = states.id)

    params = {
        'all_shops' : all_shop,
        'all_city' : all_city,
        'all_state' : all_state,
    }

    return render(request, 'shop_list_layout.html',params)

def costomer_logout(request):
    logout(request)
    return redirect('/')

def costomer_login(request):

    username = request.POST['login_username']
    password = request.POST['login_password']
    user = authenticate(username = username, password = password)

    if user is not None:

        confirm_user = customer.objects.filter(full_name = username)
        # print(len(confirm_user))
        
        if len(confirm_user) !=0 :
            login(request, user)
            global var
            def var():
                return username

            return redirect('/')
        else:
            return HttpResponse("this is not the way my boy")
    else :
        return HttpResponse("not a customer")

def shop_page_layout(request):

    return render(request, 'shop_page_layout.html')

def shop_list_layout(request):

    all_state = state.objects.all()
    all_shops = seller_shop_details.objects.all()

    params = {
        'all_shops' : all_shops,
        'all_state' : all_state,
        }

    return render(request, 'shop_list_layout.html',params)

def grocery_shop_list_layout(request):

    grocery_shops = seller_shop_details.objects.filter(shop_category = 'Grocery')
    params = {
        'all_shops' : grocery_shops
    }
    return render(request , 'shop_list_layout.html', params)

def stationery_shop_list_layout(request):
    stationery_shops = seller_shop_details.objects.filter(shop_category = 'Stationery')

    params = {
        'all_shops' : stationery_shops
    }
    return render(request , 'shop_list_layout.html', params)

def cloth_shop_list_layout(request):

    cloth_shops = seller_shop_details.objects.filter(shop_category = 'clothes')
    params = {
        'all_shops' : cloth_shops
    }
    return render(request , 'shop_list_layout.html', params)
    
def bakery_shop_list_layout(request):
    bakery_shops = seller_shop_details.objects.filter(shop_category = 'Bakery')

    params = {
        'all_shops' : bakery_shops
    }
    return render(request , 'shop_list_layout.html', params)


def home_page(request):

    states = state.objects.all()
    cities = city.objects.all()

    params = {
        'all_state' : states,
        'all_city' : cities
    }
    return render(request, 'costomer/home_page.html', params)

def contactus_page (request):
    return render(request, 'costomer/contactus_page.html')

def costomer_profile(request):
    userid = var()

    costomer_data = customer.objects.get( full_name = userid )
    all_orders = order.objects.filter(costomer_name = userid)

    params = {
        'costomer_data' : costomer_data,
        'all_orders' : all_orders
    }
    return render(request, 'costomer/costomer_profile.html',params)
 
def aboutus_page(request):
    return render(request, 'costomer/aboutus_page.html') 

def registration_page(request):
    if request.method == "POST":
        full_name = request.POST['full_name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        password = request.POST['password'] 
        confirm_password = request.POST['confirm_password']
        states = request.POST['input_state']
        citys = request.POST['input_city']
        zip_code = request.POST['input_zip']
        land_mark = request.POST['land_mark']
        address = request.POST['address']
        costomer_image = request.FILES.get('costomer_image')
         
        # print(costomer_image)

        state_id = state.objects.get(state_name = states)
        city_id = city.objects.get(city_name = citys) 

        myuser = User.objects.create_user(full_name, email, password)
        myuser.save()

        if password != confirm_password :
            return HttpResponse("password dont match")
 
        ins = customer(full_name = full_name, phone_number = phone_number ,email = email , password = password , confirm_password = confirm_password , zip_code = zip_code, land_mark = land_mark , address = address,
                        state = state_id, city = city_id , costomer_img = costomer_image)
        ins.save()

        params = {
            'success' : 'user is created successfully',
        }

        return redirect('/', params)
    else :
        return HttpResponse("you cant access the registration page from only url")