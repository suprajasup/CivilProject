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

def screen3a(request):
	
	return render(request,"screen3a.html")

def screen3b(request):
	
	return render(request,"screen3b.html")

def screen3c(request):
	
	return render(request,"screen3c.html")

def screen6(request):
	
	return render(request,"screen6.html")


def screen7(request):
	
	return render(request,"screen7.html")

def screen8(request):
	
	return render(request,"screen8.html")

def screen8a(request):
	
	return render(request,"screen8a.html")

def screen9(request):
	
	return render(request,"screen9.html")
