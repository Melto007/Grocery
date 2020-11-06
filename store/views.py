from django.db import models
from django.views.generic.edit import CreateView
from django.contrib.auth.models import auth,User
from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import *

class HomeView(TemplateView):
    templatename = 'home.py'
    def get(self,request):
        categories = Categories.objects.all()
        foods = Foods.objects.filter(category_id=1).order_by('id')[:20]
        cuisine = Cuisine.objects.all()
        product = Foods.objects.all()
        context ={'categories':categories,'foods':foods,'cuisine':cuisine,'product':product}
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