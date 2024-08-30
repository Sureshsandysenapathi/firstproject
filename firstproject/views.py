from django.shortcuts import render
from django.http import HttpResponse
from demoapp.models import Blog

def home(request):
    post=Blog.objects.all()
  
    return render(request,"base.html",{'post':post})
def demo(request):
    return HttpResponse("suresh is learing django")