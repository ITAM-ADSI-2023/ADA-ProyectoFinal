from django.shortcuts import render
from django.shortcuts import render,redirect

# Create your views here.
def login(request):
    return render(request,'login.html')
def task(request):
    return render(request,'task.html')
def dasboard(request):
    return render(request,'dasboard.html')
def centroCasos(request):
    return render(request,'centroCasos.html')