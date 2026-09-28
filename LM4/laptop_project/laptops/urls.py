from .import views
from django.urls import path

urlpatterns = [
    path('', views.laptop_list, name='laptop_list'),
    path('add/', views.laptop_add, name='laptop_add'),
    path('edit/<int:id>/', views.laptop_edit, name='laptop_edit'),
    path('delete/<int:id>/', views.laptop_delete, name='laptop_delete'),
]
