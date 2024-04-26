from django.urls import path, include
from . import views
from .views import user_login

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('editar/<int:id>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
    path('index', views.index, name='index'),  
    path('login/', user_login, name='login'),
]




