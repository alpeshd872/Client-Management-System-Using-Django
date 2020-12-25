from django.contrib import admin
from django.urls import path, include
from home import views
urlpatterns = [
    path("", views.dashboard, name='dashboard'),
    path("dashboard/", views.dashboard, name='dashboard'),
    path("login/", views.login, name='login'),
    path("products/", views.products, name='products'),

    path("customers/<str:cid>/", views.customers, name='customers'),

    path("update_order/<str:cid>/", views.updateOrder, name='update_order'),
    path("delete_order/<str:cid>/", views.deleteOrder, name='delete_order'),
    path("UpdateCustomer/<str:cid>/", views.UpdateCustomer, name='UpdateCustomer'),
    path("placeOrder/<str:cid>/", views.placeOrder, name='placeOrder'),
    path("createCustomer", views.createCustomer, name='createCustomer'),


]
