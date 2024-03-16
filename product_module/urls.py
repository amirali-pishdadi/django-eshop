from django.urls import path
from . import views

urlpatterns = [
    path('product-detail/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('product-favorite', views.AddFavoriteProductView.as_view(), name='add_favorite'),
    path('add_comment/', views.AddCommentView.as_view(), name='add_comment'),
    path('all-product/' , views.AllProductView.as_view() , name='all_product')
]
