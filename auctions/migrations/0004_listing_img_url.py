# Generated by Django 3.2.5 on 2021-09-01 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20210901_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='img_url',
            field=models.URLField(blank=True),
        ),
    ]
