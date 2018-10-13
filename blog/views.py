from django.shortcuts import render
from blog.models import Post

# Create your views here.
def index(request):
	post=Post()
	title=post.title
	print(title)
		


	return render(request,'blog/index.html',{'post':post})