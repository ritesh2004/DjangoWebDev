# Generated by Django 4.1.7 on 2023-04-29 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_delete_quizslots_alter_quiz_quizid'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='qnno',
            field=models.IntegerField(default=False),
        ),
    ]
