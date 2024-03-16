from django.urls import path
from . import views

urlpatterns = [
    path('add_product/', views.AddProductView.as_view(), name="add_product_page"),
    path('remove_product/', views.RemoveProductView.as_view(), name="remove_product_page"),
    path('', views.UserBaskedView.as_view(), name="user_basked"),
    path('request-payment/', views.request_payment, name='request_payment'),
    path('verify-payment/', views.verify_payment, name='verify_payment'),
]
