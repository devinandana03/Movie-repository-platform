from django.db import models
from django.contrib.auth.models import User
from movie.models import Movie

from django.db.models.signals import post_save
from PIL import Image as PilImage
from PIL import Image
from django.conf import settings
import os

# Create your models here.

def user_directory_path(instance, filename):
	profile_pic_name = 'user_{0}/profile.jpg'.format(instance.user.id)
	full_path = os.path.join(settings.MEDIA_ROOT, profile_pic_name)

	if os.path.exists(full_path):
		os.remove(full_path)
	return profile_pic_name


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	first_name = models.CharField(max_length=50, null=True, blank=True)
	last_name = models.CharField(max_length=50, null=True, blank=True)
	location = models.CharField(max_length=50, null=True, blank=True)
	url = models.CharField(max_length=80, null=True, blank=True)
	profile_info = models.TextField(max_length=150, null=True, blank=True)
	created = models.DateField(auto_now_add=True)
	to_watch = models.ManyToManyField(Movie, related_name='towatch')
	watched = models.ManyToManyField(Movie, related_name='watched')
	#picture = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
	picture = models.ImageField(upload_to=user_directory_path, blank=True, null=True)

	# def save(self, *args, **kwargs):
	# 	super().save(*args, **kwargs)
	# 	SIZE = 250, 250

	# 	if self.picture:
	# 		pic = Image.open(self.picture.path)
	# 		pic.thumbnail(SIZE, Image.LANCZOS)
	# 		pic.save(self.picture.path)
def save(self, *args, **kwargs):
        if self.picture:
            pil_image = PilImage.open(self.picture)
            if pil_image.mode != 'RGB':
                pil_image = pil_image.convert('RGB')
            pil_image.save(self.picture.path)
        super(Profile, self).save(*args, **kwargs)  # Call the super() method from here

def __str__(self):
		return self.user.username

def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()


post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
