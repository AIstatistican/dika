# Generated by Django 5.0.6 on 2024-07-08 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='howFoundUs',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Bizi nereden buldunuz'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='inputAge',
            field=models.DateField(blank=True, null=True, verbose_name='Doğum tarihiniz'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='inputCity',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Yaşadığınız şehir'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='inputGender',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Cinsiyetiniz'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='inputName',
            field=models.CharField(max_length=100, verbose_name='Adınız'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='inputPassword1',
            field=models.CharField(max_length=100, verbose_name='Şifreniz'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='inputPassword2',
            field=models.CharField(max_length=100, verbose_name='Şifreniz tekrardan'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='inputPhoneNumber',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefon numaranız'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='inputSurname',
            field=models.CharField(max_length=100, verbose_name='Soyadınız'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='inputUniversity',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Mezun olduğunuz üniversite'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='inputUsername',
            field=models.EmailField(max_length=254, verbose_name='Kullanıcı adınız'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='inputkurum',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Çalıştığınız kurum'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='interestAreas',
            field=models.TextField(blank=True, null=True, verbose_name='İlgilendiğiniz alan'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(blank=True, null=True, verbose_name='Mesajınız'),
        ),
    ]
