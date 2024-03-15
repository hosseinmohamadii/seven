from django.urls import path
from .views import new, register, userlogin, userlogout,listc

urlpatterns = [
    path('new/', new, name='new'),
    path('login/', userlogin, name='login'),
    path('signup/', register, name='register'),
    path('logout/', userlogout, name='logout'),
     path('list/', listc, name='all-c'),  
]
