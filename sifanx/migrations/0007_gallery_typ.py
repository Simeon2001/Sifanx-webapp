# Generated by Django 3.0.2 on 2020-01-26 21:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sifanx', '0006_feedback_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='typ',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]
