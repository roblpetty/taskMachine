# Generated by Django 2.1.3 on 2018-12-15 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_post_date_edited'),
    ]

    operations = [
        migrations.CreateModel(
            name='Substask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskId', models.IntegerField()),
                ('subtaskId', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='date_edited',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
