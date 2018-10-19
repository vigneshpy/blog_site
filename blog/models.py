from django.db import models
from django.utils import timezone


class Post(models.Model):
	title=models.CharField(max_length=264)
	author=models.ForeignKey('auth.user',on_delete=models.CASCADE)
	text=models.CharField(max_length=264)
	created_date=models.DateTimeField(default=timezone.now())
	pub_date=models.DateTimeField(blank=True,null=True)

	def publish(self):
		self.pub_date = timezone.now()
		self.save()
	
	def __str__(self):
		return self.title
	def body(self):
		return self.text[:100]
# Create your models here.
