from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserInfoModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    # additional details

    portfolio_site = models.URLField(blank=True)
    portfolio_image = models.ImageField(upload_to = 'portfolio_pics', blank=True)

    def __str__(self):
        return self.user.username
