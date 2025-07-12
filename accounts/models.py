from django.db import models
from django.conf import settings
import random

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', default='default.jpg')
    is_verified = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=6, blank=True)

    def generate_code(self):
        code = str(random.randint(100000, 999999))
        self.verification_code = code
        self.save()
        return code

    def __str__(self):
        return f"{self.user.username}'s profile"
