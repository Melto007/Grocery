from django.db import models
from django.views.generic.edit import CreateView
from django.contrib.auth.models import auth,User
from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from django.contrib import messages

class HomeView(TemplateView):
    templatename = 'home.py'
    def get(self,request):
        return render(request,self.templatename)
        
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

