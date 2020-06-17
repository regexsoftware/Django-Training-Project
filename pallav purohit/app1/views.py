from django.db.models import Q
from django.shortcuts import render, HttpResponse, redirect
from.models import Employee
from.models import image
from.models import Zomato
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from rest_framework import generics
from rest_framework.response import Response
import csv, io 
from tablib import Dataset
from .models import zoamto
from django.contrib.sessions.models import Session
# Create your views here.

#def aa():
#    print("hello man how are you")

def hello(request):
    
    return render(request, 'pallav.html')

###xyz##
def is_validpara(param):
    return param != '' and param is not None


##businessman
def fart(request):

    a = Employee.objects.all()
    b = image.objects.all()
    qs =Zomato.objects.all()
    qo =zoamto.objects.all()
    count = 0
    flag = 0
    lag = 0
    
    if request.method == 'POST':
        print("hi")
        First_name = request.POST.get('first_name')
        Last_name = request.POST.get('last_name')
        sippi_query = request.POST.get('halo')
        carry_pop = request.POST.get('CUISINE_TYPE')
        rating = request.POST.get('rating')

        user = Employee()
        user.first_name = First_name
        user.last_name = Last_name
        user.save()
    
        if is_validpara(sippi_query):
            lag = 1
            qo = qo.filter(CITY=sippi_query)
            if is_validpara(carry_pop):
                flag = 1
                print ("nalo")   
                qo = qo.filter(CUISINECATEGORY__icontains= carry_pop)
                if is_validpara(rating):
                    qo = qo.filter(RATING__gte = rating)
                    count = qo.all().count()
                    print(count)
            else:
                print("hello")
        
    context = {
        'queryset' : qo,
        'count':count,
        
        
    }
        

    return render(request, 'pallav.html', context)
   # return HttpResponse(a)

##customer
def zartt(request):
    a = Employee.objects.all()
    b = image.objects.all()
    qs =Zomato.objects.all()
    qo =zoamto.objects.all()
    count = 0
    flag = 0

    
    if request.method == 'POST':
        print("hi")
        First_name = request.POST.get('first_name')
        Last_name = request.POST.get('last_name')
        sippi_query = request.POST.get('halo')
        carry_pop = request.POST.get('CUISINE_TYPE')

        user = Employee()
        user.first_name = First_name
        user.last_name = Last_name
        user.save()

        if is_validpara(sippi_query):
            qo = qo.filter(CITY=sippi_query)
            print(count)
            if is_validpara(carry_pop):
                 print ("nalo")   
                 qo = qo.filter(CUISINECATEGORY__icontains= carry_pop)
                 count = qo.all().count()
                 print(count)
                 
        else:
            return redirect('index') 
  
    context = {
        'queryset' : qo,
        'count' : count


    }
        

    return render(request, 'zomato.html', context)   


def registerPage(request):
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'register.html', context)


##dashboard
def software(request):
    
        return render(request, 'tampo.html')
   

 
def loginPage(request):
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('dashboard')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)





def logoutUser(request):
	logout(request)
	return redirect('login')


def contact(request):
    return render(request, 'contact.html')    

def index(request):
    qs = Zomato.objects.all()
    a = Employee.objects.all()
    if request.method == 'POST':
        print("hi")
        First_name = request.POST.get('first_name')
        Last_name = request.POST.get('last_name')
        sippi_query = request.POST.get('halo')
        carry_pop = request.POST.get('CUISINE_TYPE')

        user = Employee()
        user.first_name = First_name
        user.last_name = Last_name
        user.save()
    
        if is_validpara(sippi_query):
            qs = qs.filter(City=sippi_query)
            count = qs.all().count()
            print(count)
            if is_validpara(carry_pop):
                print ("nala supara")   
                qs = qs.filter(Cuisines__icontains= carry_pop)
            else:
                print("hello")
    context = {
    'queryset' : qs
        
    }        

    return render(request,'pallav.html',context)