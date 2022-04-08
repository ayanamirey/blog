# Generated by Django 4.0.3 on 2022-04-08 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Title')),
                ('text', models.TextField(verbose_name='Text')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('publish_date', models.DateTimeField(auto_now_add=True, verbose_name='Publish Date')),
            ],
        ),
    ]