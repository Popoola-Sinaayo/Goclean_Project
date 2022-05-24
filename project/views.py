from django.shortcuts import render
from django.contrib.auth.models import User
from .models import User_Info
# Create your views here.


def home(request):
    return render(request, 'index.html')

def new(request):
    #Adding this to test aters
    return render(request, 'index.html')

def contact(request):
    if request.method == "GET":
        return render(request, 'contact.html')
    elif request.method == "POST":
        name = request.POST["name"]
        email = request.POST['email']
        pickup_address = request.POST['pickup']
        phone = request.POST['phone']
        quantity = request.POST['quantity']
        info = User_Info(name=name, email=email, pickup_address=pickup_address,
                         phone_number=phone, quantity_of_goods=quantity)
        info.save()
        return render(request, 'blog.html')

def blog(request):
    return render(request, 'blog.html')
