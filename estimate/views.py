from django.shortcuts import render,redirect
from django.http import HttpResponse

def home(request):
	
	return render(request,"screen1_home.html")

def screen2(request):
	
	return render(request,"screen2_signup.html")
def screen3(request):
	
	return render(request,"screen3.html")

def screen4(request):
	
	return render(request,"screen4.html")
def screen5(request):
	
	return render(request,"screen5.html")

