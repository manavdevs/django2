from django.urls import path
from . import views

urlpatterns=[
    path('',views.chome,name='clothes_home'),
    path('add/', views.chome_add, name='chome_add'), 
    path('<int:pk>/edit/', views.clothes_edit, name='clothes_edit'),
    path('<int:pk>/delete/', views.clothes_delete, name='clothes_delete'),
]