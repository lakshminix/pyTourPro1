from django.urls import path, include
from django.urls import path
from.import views

urlpatterns = [


    #for credentials app
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')
]