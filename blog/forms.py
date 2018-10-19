from blog.models import Post
from django import forms

class PostAdd(forms.ModelForm):

	class Meta:
		model=Post
		fields=('title','text')
	
			
			