from django.urls import path
from .views import new, usersignup, user_login, userlogout

urlpatterns = [
    path('signup/', usersignup, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', userlogout, name='logout'),
    path('new/', new, name='new'),
]
