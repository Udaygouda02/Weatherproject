from django.shortcuts import render
from django.contrib import messages
import requests
import datetime

def home(request):
    if 'city' in request.POST:
         city = request.POST['city']
    else:
         city = 'Bengaluru' 
    
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={{Enter api key}}'
    PARAMS = {'units':'metric'}
    
    try:
        data = requests.get(url,PARAMS).json()

        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        day = datetime.date.today()

        return render(request,'weatherapp/index.html',{'description':description , 'icon':icon ,'temp':temp , 'day':day,'city':city,'exception_occurred':False})

    except KeyError:
          exception_occurred = True
          messages.error(request,'Entered data is not available to API')   
          # city = 'indore'
          # data = requests.get(url,params=PARAMS).json()
          
          # description = data['weather'][0]['description']
          # icon = data['weather'][0]['icon']
          # temp = data['main']['temp']
          day = datetime.date.today()

          return render(request,'weatherapp/index.html' ,{'description':'clear sky', 'icon':'01d'  ,'temp':25 , 'day':day , 'city':'bengaluru' , 'exception_occurred':True} )
