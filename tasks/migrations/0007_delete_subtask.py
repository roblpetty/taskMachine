# Generated by Django 2.1.3 on 2018-12-17 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_post_children'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Subtask',
        ),
    ]
