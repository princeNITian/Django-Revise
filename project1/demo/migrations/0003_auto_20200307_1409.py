# Generated by Django 2.2.10 on 2020-03-07 08:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20200307_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=36, unique=True),
            preserve_default=False,
        ),
    ]