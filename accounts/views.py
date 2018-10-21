from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
	if request.method=='POST':
		if request.POST['p1']==request.POST['p2']:
			try:
				user=User.objects.get(username=request.POST['name'])
				return render(request,'account/signup.html',{'error':'UserName Already Exists'})
			except User.DoesNotExist:
				print("Except block executing")
				created_user=User.objects.create_user(request.POST['name'],password=request.POST['p1'])
				auth.login(request,created_user)
				return  redirect('home')
		else:
			return render(request,'account/signup.html',{'error':'Password Does Not Match'})

	else:
		print('execting')
		return render(request,'account/signup.html')

def login(request):
	if request.method=='POST':
		user=auth.authenticate(username=request.POST['name'],password=request.POST['p1'])
		print(user)
		if user is None:
			return render(request,'account/login.html',{'error':' Invalid User Name or Password '})
		else:
			auth.login(request,user)
			return render(request,'products/home.html',{'success':' Logged in Success '})

	return render(request,'account/login.html')


def logout_(request):
	auth.logout(request)
	return render(request,'account/logout.html')
# Create your views here.
