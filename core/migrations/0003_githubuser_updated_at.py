# Generated by Django 3.0.3 on 2020-02-06 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_githubuser_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='githubuser',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]