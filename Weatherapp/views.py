from django.shortcuts import render
from .forms import MyForm
import json
import urllib
from django.shortcuts import redirect

def index(request):
    form = MyForm()
    context = {"form":form}
    
    if request.method == "POST":
        form = MyForm(request.POST)
        context = {"form":form}
        if form.is_valid():
            city = form.cleaned_data["city"]
            
            response = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=Your_api_key").read()
            
            data = json.loads(response)
            data_clean = {
                    "city": city,
                    'lon': str(data['coord']['lon']),
                    'lat': str(data['coord']['lat']),
                    "weather_condition": str(data['weather'][0]['main']),
                    "weather_des":str(data['weather'][0]['description']),
                    "temp": str(int(data['main']['temp'])-273.5),
                    "feels_like": str(int(data['main']['feels_like'])-273.5),
                    "temp_max": str(int(data['main']['temp_max'])-273.5),
                    "temp_min": str(int(data['main']['temp_min'])-273.5),
                    "humidity": str(data['main']['humidity']),
                    "wind": str(data['wind']['speed']),
                }
            context['data'] = data_clean
            
            context["form"] = form
            return render(request,"Weatherapp/index.html",context)

        else:
            return render(request,"Weatherapp/index.html",context)
    return render(request,"Weatherapp/index.html",context)