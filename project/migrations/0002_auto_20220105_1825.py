# Generated by Django 3.0.8 on 2022-01-06 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_info',
            name='user',
        ),
        migrations.AddField(
            model_name='user_info',
            name='email',
            field=models.EmailField(default='None', max_length=254),
        ),
        migrations.AddField(
            model_name='user_info',
            name='name',
            field=models.CharField(default='None', max_length=1000),
        ),
    ]
