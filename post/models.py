from django.db import models
from django.urls import reverse



# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=200, verbose_name="Başlık")
    content=models.TextField(verbose_name="Metin")
    publishing_date=models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'id':self.id })
       # return "/post/{}".format(self.id)