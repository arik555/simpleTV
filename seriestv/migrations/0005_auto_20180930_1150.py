# Generated by Django 2.1.1 on 2018-09-30 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seriestv', '0004_auto_20180927_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='compatible',
            field=models.CharField(choices=[('0', 'None'), ('1', 'Clappr'), ('2', 'YouTube'), ('3', 'OpenLoad'), ('4', 'jWplayer')], default='3', max_length=1),
        ),
    ]
