# Generated by Django 4.1 on 2022-11-19 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0005_tprofile_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tprofile',
            name='contact',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
