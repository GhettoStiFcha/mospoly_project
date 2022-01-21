# Generated by Django 4.0.1 on 2022-01-21 08:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mysite', '0002_music_image_alter_music_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]