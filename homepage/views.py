from django.shortcuts import render

def home(request):
    return render(request,'homepage/home.html')

def instagram(request):
    return render(request,'homepage/instagram.html')