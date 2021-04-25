from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Home(request):
    return render(request,'htmltestapp/Home.html')

def index(request):
    return render(request,'htmltestapp/index.html')
def contact(request):
    return render(request,'htmltestapp/Contact.html')
def about(request):
    return render(request,'htmltestapp/About.html')
