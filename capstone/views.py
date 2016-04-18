from django.http import HttpResponse
from django.shortcuts import render
import json

# Create your views here.
from capstone import dao


def home(request):
    return render(request,'crash_report.html',{})

def upload(request):
    return render(request,'uploader.html',{})

def getMajorFatal(request):
    crashes=dao.getMajFatalCrash();
    list=[]
    for crash in crashes:
        data={}
        data['lat']=crash.lat
        data['lng']=crash.lng
        data['crn']=crash.crn
        list.append(data)
    return HttpResponse(json.dumps(list))