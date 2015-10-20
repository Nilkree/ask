from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.
class Question(models.Model):
	from_user = models.ForeignKey(User, related_name='sent_questions', blank = True, null = True)
	to_user = models.ForeignKey(User, related_name='get_questions', blank = True, null = True)
	text = models.TextField(null = True)
	answered = models.BooleanField(default = False)
	created = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.text

	def get_absolute_url(self):
		return reverse('site:make_answer', args=[str(self.id)])

class Answer(models.Model):
	question = models.OneToOneField(Question, blank = True, null = True)
	text = models.TextField(null = True)
	created = models.DateTimeField(auto_now_add = True)
	likes = models.IntegerField(default = 0, blank = True)

	def __str__(self):
		return self.text
