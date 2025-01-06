from django.urls import path
from . import views

urlpatterns=[
    path('',views.ehome,name='elec_home'),
    path('add/', views.elec_add, name='elec-add'), 
    path('<int:pk>/edit/', views.elec_edit, name='elec_edit'),
    path('<int:pk>/delete/', views.elec_delete, name='elec_delete'),
]