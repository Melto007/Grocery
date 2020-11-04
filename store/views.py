from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    templatename = 'home.py'
    def get(self,request):
        return render(request,self.templatename)

