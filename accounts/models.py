

# Create your models here.


# models.py
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser





class Contact(models.Model):
    inputName = models.CharField(max_length=100, verbose_name='Adınız')
    inputSurname = models.CharField(max_length=100,verbose_name='Soyadınız')
    inputAge = models.DateField(blank=True, null=True,verbose_name='Doğum tarihiniz')
    inputGender = models.CharField(max_length=10,blank=True, null=True,verbose_name='Cinsiyetiniz')
    inputPhoneNumber = models.CharField(max_length=20,blank=True, null=True,verbose_name='Telefon numaranız')
    inputUniversity = models.CharField(max_length=100, blank=True, null=True,verbose_name='Mezun olduğunuz üniversite')
    inputCity = models.CharField(max_length=100,blank=True, null=True,verbose_name='Yaşadığınız şehir')
    inputkurum = models.CharField(max_length=100, blank=True, null=True,verbose_name='Çalıştığınız kurum')
    inputUsername = models.EmailField(verbose_name='Kullanıcı adınız')
    inputPassword1 = models.CharField(max_length=100, verbose_name='Şifreniz')
    inputPassword2 = models.CharField(max_length=100, verbose_name='Şifreniz tekrardan')
    interestAreas = models.TextField(blank=True, null=True,verbose_name='İlgilendiğiniz alan')  # Adjust as per your form requirements
    howFoundUs = models.CharField(max_length=100,blank=True, null=True,verbose_name='Bizi nereden buldunuz')
    message = models.TextField(blank=True, null=True,verbose_name='Mesajınız')

    def __str__(self):
        return f"{self.inputName} {self.inputSurname}" # bunun amacı kayıtları ad ve soyad ile birbirinden ayırma admin sayfasında yada buraya başka bir karakteri de verebilirsin
        

    def get_absolute_url(self):
        return reverse('accounts:contact_detail', kwargs={'id':self.id })
    

       # return "/post/{}".format(self.id) 




