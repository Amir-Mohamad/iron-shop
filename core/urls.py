from django.urls import path
from . import views


app_name='core'
urlpatterns = [
    path('', views.products_list, name="product_list"),
    path('<slug:category_slug>/', views.products_list, name="product_list_by_category"),
    path('<int:id>/<slug:slug>/', views.product_detail, name="product_detail"),
]
