from django.contrib import admin
from django.urls import path
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('',views.HomeView.as_view(),name='home'),
  
   path('register_data',views.Register_user.as_view(),name='register_data'),
   path('login_data',views.Login_user.as_view(),name='login_data'),
   path('logout_action',views.Login_user.as_view(),name='logout_action'),
   
   path('update_item/',views.Update_Item.as_view(),name='update_item'),
   path('cat_selection',views.HomeView.as_view(),name='cat_selection'),

   path('search_details',views.Search_Details.as_view(),name='search_details'),
   path('search_data',views.Search_Details.as_view(),name='search_data'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)