# Generated by Django 2.2.2 on 2019-06-22 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crystal', '0002_auto_20190622_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='cites',
            field=models.ManyToManyField(blank=True, related_name='_publication_cites_+', to='crystal.Publication'),
        ),
    ]
