# Generated by Django 4.1.7 on 2023-04-16 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='drinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drink', models.CharField(max_length=50)),
                ('price', models.IntegerField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='foods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food', models.CharField(max_length=50)),
                ('price', models.IntegerField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='icecreams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icecream', models.CharField(max_length=50)),
                ('price', models.IntegerField(max_length=5)),
            ],
        ),
    ]