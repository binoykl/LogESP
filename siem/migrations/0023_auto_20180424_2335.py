# Generated by Django 2.0.4 on 2018-04-25 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siem', '0022_auto_20180416_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logevent',
            name='parsed_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name=6),
        ),
        migrations.AlterField(
            model_name='ruleevent',
            name='date_stamp',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
