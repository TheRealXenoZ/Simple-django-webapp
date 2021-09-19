from django.http import response
from django.shortcuts import render
import requests as r
import json as j
import datetime

# Create your views here.

def weather(request):
    if 'cty' in request.GET:
        city = request.GET['cty']
        Wtr_temp = r.get(f"https://goweather.herokuapp.com/weather/{city}")
        WeatherDict = j.loads(Wtr_temp.text)
        context = {
            'city_name' : city,
            'temperature' : WeatherDict['temperature'],
            'description' : WeatherDict['description'],
        }
    else:
        context = None
    return render(request, 'weather/weather.html', context)
    
def index(request):
    return render(request, 'weather/index.html')

def about(request):
    return render(request, 'weather/about.html')

def contact(request):
    return render(request, 'weather/contact.html')

def time(request):
    Time = str(datetime.datetime.now())
    context = { 'time' : Time}
    return render(request, 'weather/time.html', context)

def diction(request):
    if 'dict' in request.GET:
        word = request.GET['dict']
        temp = r.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")

        word_lst = j.loads(temp.text)
        word_dict = word_lst[0]

        context = {
            'word' : word,
            'phonetic' : word_dict['phonetic'],
            'origin' : word_dict['origin'],
            'meaning' : word_dict['meanings'][0]['definitions'][0]['definition'],
        }
    else:
        context = None
    print (response)
    return render(request, 'weather/dict.html', context)
