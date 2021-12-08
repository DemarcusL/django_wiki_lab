
# Create your models here.
from django.contrib.auth import get_user_model
from django.db import models

class Wiki(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(default="", max_length=100)
    poster = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


    def __str__(self):
        #  this can be used to to return different things to be used 
        return(f'{self.title} , {self.poster} ')