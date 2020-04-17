# Generated by Django 2.2.2 on 2019-08-29 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crystal', '0007_auto_20190628_2312'),
    ]

    operations = [
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='publication',
            name='network',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='crystal.Network'),
            preserve_default=False,
        ),
    ]
