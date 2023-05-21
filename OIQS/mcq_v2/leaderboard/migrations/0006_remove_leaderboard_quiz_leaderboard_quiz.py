# Generated by Django 4.1 on 2022-11-21 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_remove_quizze_lb'),
        ('leaderboard', '0005_leaderboard_quiz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaderboard',
            name='quiz',
        ),
        migrations.AddField(
            model_name='leaderboard',
            name='quiz',
            field=models.ManyToManyField(null=True, to='quiz.quizze'),
        ),
    ]
