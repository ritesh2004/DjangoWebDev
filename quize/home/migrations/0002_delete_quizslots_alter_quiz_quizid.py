# Generated by Django 4.1.7 on 2023-04-27 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='quizslots',
        ),
        migrations.AlterField(
            model_name='quiz',
            name='quizid',
            field=models.CharField(max_length=500),
        ),
    ]
