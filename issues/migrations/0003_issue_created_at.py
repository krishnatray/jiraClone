# Generated by Django 3.0.3 on 2020-04-17 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0002_auto_20200413_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]