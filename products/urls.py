from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('products/series/<int:series_id>/', views.product_list, name='product_series'),
    path('support/', views.support, name='support'),
    path('about/', views.about_us, name='about_us'),
]