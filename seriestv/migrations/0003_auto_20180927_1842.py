# Generated by Django 2.1.1 on 2018-09-27 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seriestv', '0002_auto_20180927_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='episode_link',
            field=models.CharField(max_length=1000),
        ),
    ]
