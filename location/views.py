import json
from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    my_ip = requests.get('https://api64.ipify.org?format=json')
    my_ip_data = json.loads(my_ip.text)
    res = requests.get('http://ip-api.com/json/'+my_ip_data["ip"])
    location = res.text
    location_data = json.loads(location)
    return render(request, 'index.html', {'data':location_data})