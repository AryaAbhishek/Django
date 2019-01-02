from django.db import models

# Create your models here.
class Topic(models.Model):
    Topic_name = models.CharField(max_length=255, unique = True)

    def __str__(self):
        return self.Topic_name
class WebPage(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    url = models.URLField(unique = True)

    def __str__(self):
        return self.name
class AccessRecord(models.Model):
    name = models.ForeignKey(WebPage, models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
