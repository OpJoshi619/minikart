from django.urls import path
from . import views

urlpatterns = [  
    path('', views.home_page, name="home_page"),
    path('contactus_page', views.contactus_page, name="contactus_page"),
    path('costomer_profile', views.costomer_profile, name="costomer_profile"),
    path('aboutus_page', views.aboutus_page, name="aboutus_page"),   
    path('registration', views.registration_page, name="registration_page"),   
    path('costomer_login', views.costomer_login, name="costomer_login"),   
    path('shop_list_layout', views.shop_list_layout, name="shop_list_layout"),   
    path('shop_page_layout', views.shop_page_layout, name="shop_page_layout"),   
    path('costomer_logout', views.costomer_logout, name="costomer_logout"),   
    path('grocery_shop_list_layout', views.grocery_shop_list_layout, name="grocery_shop_list_layout"),   
    path('stationery_shop_list_layout', views.stationery_shop_list_layout, name="stationery_shop_list_layout"),   
    path('cloth_shop_list_layout', views.cloth_shop_list_layout, name="cloth_shop_list_layout"),   
    path('bakery_shop_list_layout', views.bakery_shop_list_layout, name="bakery_shop_list_layout"),   
    path('input_state', views.input_state, name="input_state"),   
    path('show_shop', views.show_shop, name="show_shop"),   
    # path('buy_items', views.buy_items, name="buy_items"),   
    path('buy_orders/<int:id>', views.buy_orders, name="buy_orders"),  
    path('buy_orders/place_order', views.place_order, name="place_order"),
] 
 
