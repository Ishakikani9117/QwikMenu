from django.contrib import admin
from enroll.models import kitchen, login, create_acc
# Register your models here.

admin.site.register(login)
admin.site.register(create_acc)
admin.site.register(kitchen)
# admin.site.register(QRCode)