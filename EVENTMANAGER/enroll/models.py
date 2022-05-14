from cProfile import label
from statistics import mode
from unicodedata import category
from django.db import models
from django import forms
import datetime

# import qrcode
from io import BytesIO
from django.core.files import File
# from PIL import Image, ImageDraw

# Create your models here.
    

class login(models.Model):
    uname = models.CharField(max_length = 256)
    upass = models.CharField(max_length = 256)

class create_acc(models.Model):
    fname = models.CharField(max_length = 256)
    lname = models.CharField(max_length=256)
    hemail = models.EmailField()
    uname = models.CharField(max_length=256)
    pswd = models.CharField(max_length=256)
    mobno = models.CharField(max_length=256)

class kitchen(models.Model):
    item = models.CharField(max_length=256)
    price = models.IntegerField(null=True)
    desc = models.CharField(max_length=256, null=True)

class OrderItem(models.Model):
    name = models.CharField(max_length=20, null=True)
    price = models.CharField(max_length=100,null=True,blank=True)
    quantity = models.PositiveIntegerField(default=1)


# class QRCode(models.Model):
#     url = models.URLField(blank=True)
#     image = models.ImageField(upload_to='qrcode', blank=True)

#     def save(self, *args, **kwargs):
#         qrcode_img = qrcode.make(self.url)
#         canvas = Image.new('RGB', (300, 300), 'white')
#         draw = ImageDraw.Draw(canvas)
#         canvas.paste(qrcode_img)
#         fname = f'image-{self.url}'+'.png'
#         buffer = BytesIO()
#         canvas.save(buffer, 'PNG')
#         self.image.save(fname,File(buffer),save=False)
#         canvas.close()
#         super().save(*args, **kwargs)