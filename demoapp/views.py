from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact
from .models import Blog

# Create your views here.


def home(request):
    
    post=Contact.objects.all()
    post=Blog.objects.all()
    return render(request,"base.html",{'post':post})
def first(request):
    return render(request,"first.html",{"name":"suresh"})
def demo(request):
    post=Contact.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        image=request.FILES.get('image')
        k=Contact(name=name,email=email,message=message,image=image)
        k.save()
    return render(request,"demo.html")