from django.db import models
# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "instagram.settings")
#
# import django
# django.setup()

# Create your models here.
class Feed(models.Model):
    content = models.TextField()
    image = models.TextField()
    profile_image = models.TextField()
    user_id = models.TextField()
    like_count = models.IntegerField()
     