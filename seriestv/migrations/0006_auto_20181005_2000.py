# Generated by Django 2.1.1 on 2018-10-05 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seriestv', '0005_auto_20180930_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='series_rel', to='seriestv.Series'),
        ),
    ]
