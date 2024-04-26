from django.contrib import admin
from django.urls import path, include
from productos.views import user_login
# from . import views


urlpatterns = [
    path('productos/', include('productos.urls')),
    path('admin/', admin.site.urls),
    # path('', user_login, name='login')
]
