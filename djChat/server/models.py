from django.db import models
from django.conf import settings
# Create your models here.

 
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name
    

class Server(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='sever_owner')   # on_delet = cascade means if owner is deleted than server will also be deleted of that owner 
    category = models.ForeignKey(Category,on_delete=models.PROTECT,related_name='server_category') 
    description = models.TextField(max_length=250,null=True,blank=True)
    member = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='server_member')
    
    def __str__(self):
        return self.name


class Channel(models.Model):
    name= models.CharField(max_length=100)
    owner= models.ForeignKey(settings.AUTH_USER_MODEL,related_name='channel_owner',on_delete=models.CASCADE)
    topic = models.CharField(max_length=100)
    server = models.ForeignKey(Server,on_delete= models.CASCADE, related_name='channel_server')

    def save(self, *args, **kwargs):
        self.name= self.name.lower()
        return super(Channel,self).save(*args, **kwargs)
    def __str__(self):
        return self.name