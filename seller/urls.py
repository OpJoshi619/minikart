from django.urls import path, include
from . import views

urlpatterns = [
    path('seller_home_page/<int:id>/', views.home_page, name="home_page_seller"),
    #path('seller_home_page', views.home_page, name="home_page"),
    path('seller_order_page', views.order_page, name="order_page"),
    path('seller_contact_page', views.contact_seller, name="contact_seller"),
    path('seller_registration_page', views.registration_page, name="registration_page"),
    path('add_items', views.add_items, name="add_items"),
    path('login', views.seller_login, name="seller_login"),
    path('seller_logout', views.seller_logout, name="seller_logout"),
    path('go_to_shop/<int:id>/', views.go_to_shop, name="go_to_shop"),
    # path('buy_orders/<int:id>', views.buy_orders, name="buy_orders")
    
]    

