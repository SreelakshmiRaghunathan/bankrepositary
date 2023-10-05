from . import views
from django.urls import path
urlpatterns=[

    path('register', views.register, name='register'),
    path('registration', views.registration, name='registration'),
    path('demo', views.demo, name='demo'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]
