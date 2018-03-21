from django.shortcuts import render
from django.http import HttpResponse
from display.models import Devices, Tips
import json

# Create your views here.

def index(request):
    return render(request,'index.html')

def devices(request):
    devices_list = Devices.objects.all().order_by('location')
    return HttpResponse(json.dumps(devices_list),content_type='applicatiion/json')
    