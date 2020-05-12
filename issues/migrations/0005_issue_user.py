# Generated by Django 3.0.3 on 2020-05-12 15:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('issues', '0004_auto_20200421_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='issues', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]