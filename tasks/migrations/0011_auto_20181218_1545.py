# Generated by Django 2.1.3 on 2018-12-18 15:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0010_auto_20181218_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='post',
            unique_together={('author', 'title')},
        ),
    ]
