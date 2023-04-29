# Generated by Django 4.1.7 on 2023-04-27 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quizid', models.IntegerField()),
                ('qn', models.CharField(max_length=1000)),
                ('Op_a', models.CharField(max_length=1000)),
                ('Op_b', models.CharField(max_length=1000)),
                ('Op_c', models.CharField(max_length=1000)),
                ('Op_d', models.CharField(max_length=1000)),
                ('correct', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='quizslots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quizid', models.IntegerField()),
            ],
        ),
    ]
