from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post
from blog.forms import PostAdd
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.conf import settings
import json
import urllib
import requests

# Create your views here.
def index(request):
	post=Post.objects.all()
	
	

	return render(request,'blog/index.html',{'post':post})


def details(request,pid):

	post=Post.objects.get(pk=pid)

  

	return  render(request,'blog/details.html',{'post':post})

def logout_(request):
	auth.logout(request)
	return render(request,'account/logout.html',{'logout_':'You Have Logged Out!'})

def signup(request):
	if request.method=='POST':
		if request.POST['p1']==request.POST['p2']:
			try:
				user=User.objects.get(username=request.POST['name'])
				return render(request,'account/signup.html',{'error':'UserName Already Exists'})
			except User.DoesNotExist:
				recaptcha_response = request.POST.get('g-recaptcha-response')
				data = {
					'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
					'response': recaptcha_response
					}
				r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
				result = r.json()
				if result['success']:
					created_user=User.objects.create_user(request.POST['name'],password=request.POST['p1'])
					auth.login(request,created_user)
					return  redirect('login')
				else:
					return render(request,'account/signup.html',{'error':'Invalid reCAPTCHA'})
		else:
			
			return render(request,'account/signup.html',{'error':'Password Does Not Match'})


		
	return render(request,'account/signup.html')

def login(request):
	if request.method=='POST':
		user=auth.authenticate(username=request.POST['name'],password=request.POST['p1'])
		if user is None:
			return render(request,'account/login.html',{'error':' Invalid User Name or Password '})
		else:
			auth.login(request,user)
			return redirect('index')


	return render(request,'account/login.html')

@login_required(login_url='login')
def create(request):
	pe=PostAdd()
	if request.method=="POST":
		pe=PostAdd(request.POST)
		
		if pe.is_valid():
			''' Begin reCAPTCHA validation '''
		
			''' End reCAPTCHA validation '''
			post=pe.save(commit=False)
			print(post)
			post.author=request.user
			print(post.author)
			post.pub_date=timezone.now()
			post.save()
			return render(request,'blog/create.html',{'error':"Added Successfully"})
	return render(request,'blog/create.html',{'adds':pe})


@login_required(login_url='login')
def edit(request,pk):
	post=get_object_or_404(Post,pk=pk)
	Pe=Post.objects.get(pk=pk)
	if request.method=='POST':
			form = PostAdd(request.POST, instance=post)
			if form.is_valid():
				post = form.save(commit=False)
				post.author = request.user
				post.pub_date = timezone.now()
				post.save()
				return redirect('edit', pk=post.pk)

	else:
		print("executing")
		form = PostAdd(instance=post)
	return render(request, 'blog/postedit.html', {'form':form,'post':Pe})