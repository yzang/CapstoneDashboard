from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'dashboard.html',{})

def upload(request):
    return render(request,'uploader.html',{})

def crash(request):
    return render(request, 'crash_report.html', {})

def google_map(request):
    return render(request,'maps_google.html',{})