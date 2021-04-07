from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Teacher

def teacher_profile(sender, instance, created, **kwargs):
	if created:
		group = Group.objects.get(name = 'teacher')
		instance.groups.add(group)
		Teacher.objects.create(user = instance)
		print('Profile Created')
			
post_save.connect(teacher_profile, sender = User)