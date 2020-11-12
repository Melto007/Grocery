from django.db import models
from django.views.generic.edit import CreateView
from django.contrib.auth.models import auth,User
from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import *
from django.http import JsonResponse
import json
from django.db.models import Count, F, Value
from django.db.models.functions import Length, Upper
from django.db.models import Q
from django.core.paginator import Paginator

class HomeView(TemplateView):
    templatename = 'home.py'
    def get(self,request):
        categories = Categories.objects.all()
        foods = Foods.objects.filter(category_id=1).order_by('id')[:20]
        cuisine = Cuisine.objects.all()
        products = Foods.objects.all()
        add_cart = Add_Cart.objects.all()

        paginator = Paginator(products,1)
        page = request.GET.get('page')
        product = paginator.get_page(page)


        context ={'categories':categories,'foods':foods,'cuisine':cuisine,'product':product,'add_cart':add_cart}
        return render(request,self.templatename,context)
        
    def post(self,request):
        food = request.POST['food']
        discount = request.POST['discount']
        cuisine = request.POST['cuisine']

        view_product = Foods.objects.filter(preference=food,discount__lte=discount,cuisine_id=cuisine)

        categories = Categories.objects.all()
        foods = Foods.objects.filter(category_id=1).order_by('id')[:20]
        cuisine = Cuisine.objects.all()
        product = Foods.objects.all()
        add_cart = Add_Cart.objects.all()

        context = {'view_product':view_product,'categories':categories,'foods':foods,'cuisine':cuisine,'product':product,'add_cart':add_cart}
        return render(request,self.templatename,context)

class Register_user(CreateView):
    def post(self,request):
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        Confirm_Password = request.POST['Confirm_Password']

        if password == Confirm_Password:
            if User.objects.filter(username=email):
                messages.info(request,"Email Taken")
                return redirect('/')
            else:
                insert = User.objects.create_user(email=name,username=email,password=password)
                insert.save()
                messages.info(request,'Register Successfully')
                return redirect('/')

class Login_user(CreateView):
    def get(self,request):
        auth.logout(request)
        return redirect('/')

    def post(self,request):
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(request,username=email,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('/')


class Update_Item(CreateView):
    def post(self,request):
        userid = request.POST['userid']
        product = request.POST['product']
        
        user_id = User.objects.get(id=userid)
        product_id = Foods.objects.get(id=product)

        if Add_Cart.objects.filter(foods=product_id,user_id=user_id):
            Add_Cart.objects.filter(foods=product_id,user_id=user_id).update(quantity=F('quantity')+1)
            return redirect('/')
        else:
            insert = Add_Cart.objects.create(foods=product_id,user_id=user_id,food_price=20,quantity=1)
            insert.save()
            return redirect('/')
        

       

