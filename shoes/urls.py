from django.urls import path
from . import views

urlpatterns=[
    path('',views.shome,name='shoes_home'),
    path('add/', views.shoes_add, name='shome_add'),
    path('<int:pk>/edit/', views.shoes_edit, name='shoes_edit'),
    path('<int:pk>/delete/', views.shoes_delete, name='shoes_delete'),
]