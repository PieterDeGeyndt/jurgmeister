from django.shortcuts import render,redirect

def home(request):
    return render(request,'homepage/home.html')

def instagram(request):
    return render(request,'homepage/instagram.html')

def info(request):
    return render(request,'homepage/info.html')

def pripolinfo(request):
    return redirect('pripol')

def pripol(request):
    return render(request,'homepage/pripol.html')