# Generated by Django 2.2.2 on 2019-06-28 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crystal', '0005_auto_20190628_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='year',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]