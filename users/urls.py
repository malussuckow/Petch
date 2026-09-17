
from django.urls import path
from users import views

urlpatterns = [
    path('users/',views.registerUsers,name='register'),
    path("login/",views.loginUser, name="login")
]