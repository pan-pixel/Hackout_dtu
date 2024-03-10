from django.db import models

# Create your models here.


class News_analysis(models.Model):
    company = models.CharField(max_length=255, blank=True)
    headline = models.CharField(max_length=2000)
    link = models.CharField(max_length=500)
    sentiment = models.CharField(max_length=255)


    def __str__(self):
        return self.company
