from django.contrib import admin
from .models import *


class FoodsAdminSite(admin.ModelAdmin):
    model = Foods

    fields = ['name','preference','price','discount','image','category_id','cuisine_id']

    list_display = ('name','preference','price','admin_photo','discount','category_id','cuisine_id')

class StateAdminSite(admin.ModelAdmin):
    model = State

    fields = ['cuisine_id','state_name']

    list_display = ('cuisine_id','state_name')

class CityAdminSite(admin.ModelAdmin):
    model = City

    fields = ['state_id','city_name']

    list_display = ('state_id','city_name')

admin.site.register(Categories)
admin.site.register(Cuisine)
admin.site.register(Foods,FoodsAdminSite)
admin.site.register(State,StateAdminSite)
admin.site.register(City,CityAdminSite)
admin.site.register(Add_Cart)