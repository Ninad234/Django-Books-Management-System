from django.http import HttpResponse
from django.shortcuts import render 

def home(request):
    # return HttpResponse("You are now at the Home Page")
    return render(request,'index.html')

def about(request):
    return HttpResponse("You are now at the About Page")

def contact(request):
    return HttpResponse("You are now at the Contact Page")