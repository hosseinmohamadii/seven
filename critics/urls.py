from django.urls import path
from .views import new, register, userlogin, userlogout,readc

urlpatterns = [
    path('new/', new, name='new'),
    path('login/', userlogin, name='login'),
    path('signup/', register, name='register'),
    path('logout/', userlogout, name='logout'),
    path('read/<int:id>/', readc, name='read'),  
]
