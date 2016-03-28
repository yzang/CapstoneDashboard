from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'crash_report.html',{})

def upload(request):
    return render(request,'uploader.html',{})
