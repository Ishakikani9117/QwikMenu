# Generated by Django 4.0.4 on 2022-05-12 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_delete_qrcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('price', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.DeleteModel(
            name='das',
        ),
        migrations.DeleteModel(
            name='part',
        ),
        migrations.DeleteModel(
            name='reg',
        ),
    ]
