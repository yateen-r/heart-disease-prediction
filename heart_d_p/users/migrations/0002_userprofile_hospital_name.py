# Generated by Django 3.2.25 on 2024-10-22 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='Hospital_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
