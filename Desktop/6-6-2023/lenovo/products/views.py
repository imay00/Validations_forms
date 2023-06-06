from django.shortcuts import render,redirect
from .models import Product
from products.forms import PrdForum
# Create your views here.


def prd_view(request):
    context={
        "products":Product.objects.all()
    }
    return render(request,'prd_view.html',context)

def create_view(request):
    form=PrdForum()
    if request.method=='POST':
        form=PrdForum(request.POST)
    if form.is_valid():
        form.save()
        return redirect(prd_view)
    else:
        form.errors
    context={
        "form":form    
    }
    return render(request,'create_view.html',context)

def index_view(request):
    context={
        
    }
    return render(request,'index.html',context)