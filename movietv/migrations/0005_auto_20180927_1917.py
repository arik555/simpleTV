# Generated by Django 2.1.1 on 2018-09-27 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movietv', '0004_movie_compatible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='compatible',
            field=models.CharField(choices=[('0', 'None'), ('1', 'Clappr'), ('2', 'YouTube'), ('3', 'OpenLoad')], default='1', max_length=1),
        ),
    ]