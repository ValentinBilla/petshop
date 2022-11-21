from django.urls import path
from . import views

urlpatterns = [
    path('', views.petshop, name='petshop'),
    path('animal/<str:name>/', views.animal_detail, name='animal_detail'),
    path('animal/<str:name>/?<str:message>', views.animal_detail, name='animal_detail_mes'),
]