# Generated by Django 2.1.5 on 2019-01-23 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disyo', '0003_auto_20190122_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='dsapplication',
            name='category',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dsapplication',
            name='subcategory',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
