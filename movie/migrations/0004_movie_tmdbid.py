# Generated by Django 5.0.3 on 2024-04-26 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='tmdbID',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
