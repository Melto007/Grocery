from django.contrib import admin
from django.urls import path
from . import views
from .views import *

urlpatterns = [
   path('',views.HomeView.as_view(),name='home'),
   path('register_data',views.Register_user.as_view(),name='register_data'),
]
