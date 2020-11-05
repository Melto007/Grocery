from django.contrib import admin
from .models import *


class FoodsAdminSite(admin.ModelAdmin):
    model = Foods

    fields = ['name','preference','price','discount','image']

    list_display = ('name','preference','price','admin_photo','discount')

admin.site.register(Categories)
admin.site.register(Cuisine)
admin.site.register(Foods,FoodsAdminSite)