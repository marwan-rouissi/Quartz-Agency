from django.urls import path

from .views import (
    product_create_view, 
    product_created_view,
    product_detail_view, 
    product_delete_view,
    product_download_view,
    product_update_view,
    dwd,
)

app_name = 'products'
urlpatterns = [
    path('dwd/', dwd, name='dwd'),
    path('download/', product_download_view, name='product-list'),
    path('create/', product_create_view, name='product-list'),
    path('created/', product_created_view, name='product-list'),
    path('<int:id>/', product_detail_view, name='product-detail'),
    path('<int:id>/update/', product_update_view, name='product-update'),
    path('<int:id>/delete/', product_delete_view, name='product-delete'),
]