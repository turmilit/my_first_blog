from django.db import models
from django.utils import timezone

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)

	def publish(self, pub_date=None):
		if pub_date == None:
			pub_date = timezone.now()
		self.published_date = pub_date
		self.save()

	def __str__(self):
		return self.title