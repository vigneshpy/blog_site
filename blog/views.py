from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post
from blog.forms import PostAdd
from django.utils import timezone

# Create your views here.
def index(request):
	post=Post.objects.all()
	
	

	return render(request,'blog/index.html',{'post':post})


def details(request,pid):

	post=Post.objects.get(pk=pid)
	print(post)

  

	return  render(request,'blog/details.html',{'post':post})


def create(request):
	pe=PostAdd()
	if request.method=="POST":
		pe=PostAdd(request.POST)
		print(pe)
		if pe.is_valid():
			post=pe.save(commit=False)
			print(post)
			post.author=request.user
			print(post.author)
			post.pub_date=timezone.now()
			post.save()
			return render(request,'blog/create.html',{'error':"Something went Wrong"})
		else:
			return render(request,'blog/create.html',{'error':"Something went Wrong"})

	

	return render(request,'blog/create.html',{'adds':pe})