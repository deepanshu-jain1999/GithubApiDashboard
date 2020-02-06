# Generated by Django 3.0.3 on 2020-02-06 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_githubuser_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=256)),
                ('min_followers', models.IntegerField(default=0)),
                ('min_repository', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
