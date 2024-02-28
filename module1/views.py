from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello1(request):
    return HttpResponse("<center>Welcome to TTM Homepage</center>")


def newhomepage(request):
    return render(request,'newhomepage.html')

def travelpackage(request):
    return render(request,"travelpackage.html")

from django.shortcuts import render
from django.http import HttpResponse

def print1(request):
    return render(request,'print_to_console.html')

def print_to_console(request):
    if request.method=="POST":
        user_input=request.POST['user_input']
        print(f'User input:{user_input}')
    a1={'user_input':user_input}
    return render(request,'print_to_console.html',a1)

import random
import string
def randomcall(request):
    return render(request,'randomOtpgenerator.html')

def randomlogic(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        print(f'User input:{user_input}')
        a2=int(user_input)
        ran1 = ''.join(random.sample(string.digits, k=a2))
        a1 = {'ran1': ran1}
        return render(request, 'randomOtpgenerator.html', a1)

from .forms import *
def getdate1(request):
    return render(request,'datetime.html')

import datetime
from django.shortcuts import render
def get_date(request):
    if request.method=='POST':
        form = IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value=form.cleaned_data['integer_value']
            date_value=form.cleaned_data['date_value']
            updated_date=date_value+datetime.timedelta(days=integer_value)
            return render(request,'datetime.html',{'updated_date':updated_date})
        else:
          form=IntegerDateForm()
        return render(request,'datetime.html',{'form':form})

def get_registered(request):
    return render(request, 'anyfile.html')

from.models import *
from django.shortcuts import render, redirect
def registerloginfunction(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phonenumber = request.POST.get('phonenumber')
        if Bhavya.objects.filter(email=email).exists():
            return HttpResponse("Email already registered.Choose a different email.")
        Bhavya.objects.create(name=name, email=email, password=password, phonenumber=phonenumber)
        return redirect('newhomepage')
    return render(request,'anyfile.html')

def contact123(request):
    return render(request, 'contact.html')

from.models import *
from django.shortcuts import render, redirect
def contactmail(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        comments = request.POST.get('comments')
        data=contactus(name=name, email=email, password=password, phonenumber=phonenumber)
        data.save()
        return redirect('newhomepage')
    return render(request,'contact.html')

import matplotlib.pyplot as plt
import numpy as np

def pie_chart(request):
    if request.method == 'POST':
        form = PieChartForm(request.POST)
        if form.is_valid():
            # Process user input
            y_values = [int(val) for val in form.cleaned_data['y_values'].split(',')]
            labels = [label.strip() for label in form.cleaned_data['labels'].split(',')]

            # Create pie chart
            plt.pie(y_values, labels=labels, startangle=90)
            plt.savefig('static/images/pie_chart.png')  # Save the chart image
            img1={'chart_image': '/static/images/pie_chart.png'}
            return render(request, 'pie_chart.html', img1)
    else:
        form = PieChartForm()
    return render(request, 'pie_chart.html', {'form': form})


class PieChartForm(forms.Form):
    y_values = forms.CharField(label='Y Values', help_text='Enter comma-separated values')
    labels = forms.CharField(label='Labels', help_text='Enter comma-separated labels')

def cars(request):
    return render(request,'cars.html')
'''
def weatherpagecall(request):
    return render(request,'weatherappinput.html')

def weatherlogic(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = '5bfcfef09b30de50ad0e6a236ffcda9a'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1= round(temperature - 273.15,2)
            return render
'''
'''
import requests
def weatherpagecall(request):
    return render(request, 'weatherappinput.html')

def weatherlogic(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = '3203182039938a3ce6d870493b3c15f5'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1= round(temperature - 273.15,2)
            return render(request, 'weatherappinput.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'weatherappinput.html', {'error_message': error_message})'''

def weatherpagecall(request):
    return render(request, 'weatherappinput.html')
def weatherlogic(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = '4e30ba3dcd838f557e9bdcdc536d48ad'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1 = round(temperature - 273.15,2)
            return render(request, 'weatherappinput.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'weatherappinput.html', {'error_message': error_message})