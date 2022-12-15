from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Person
from django.contrib.auth.hashers import check_password, make_password
from django.contrib import messages

def home(request):
   return render(request,"./app/home.html")

def login(request):
   return render(request,"./app/login.html")

def table(request):
   return render(request,"./app/table.html")


def update(request):
   return render(request,"./app/update.html")

def welcome(request):
   return render(request,"./app/welcome.html")

def form_data(request):
   if request.method=='POST':
      first_name=request.POST['first_name']
      last_name=request.POST['last_name']
      Company_name=request.POST['Company']
      Email_name=request.POST['Email_name']
      Phone_number=request.POST['Phone']
      Password=make_password(request.POST['Password'])
      if Person.objects.filter(Phone_number=Phone_number).exists():
             messages.error(request,'Phone Number Exists')
             return redirect('/')
      elif Person.objects.filter(Email_name=Email_name).exists():
             messages.error(request,'Email Exists')
             return redirect('/')
      else:
          Person.objects.create(first_name=first_name,last_name=last_name,Company_name=Company,Email_name=Email_name,Phone_number=Phone_number,Password=Password)
          return redirect('/login')