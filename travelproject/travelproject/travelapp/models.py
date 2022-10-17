from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pics')
    desc=models.TextField()
class Travel(models.Model):
    photo=models.ImageField(upload_to='pics')
    date=models.IntegerField()
    month=models.CharField(max_length=250)
    head = models.CharField(max_length=250)
    description= models.TextField()

    #
    # def __str__(self):
    #     return self.name