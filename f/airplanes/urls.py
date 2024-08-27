from django.urls import path
from .views import *


urlpatterns = [
    path("", index, name="index"),
    #    /aeropuertos, 
    path("aeropuertos", aeropuertos, name="aeropuertos"),
    path("login", login_view, name="login_view"),
    path("logout", logout_view, name="logout_view"),
    path("agregar", add_airport, name="agregar")
]