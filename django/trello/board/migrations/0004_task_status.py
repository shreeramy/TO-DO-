# Generated by Django 3.2.12 on 2022-06-24 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(default='TODO', max_length=50),
        ),
    ]
