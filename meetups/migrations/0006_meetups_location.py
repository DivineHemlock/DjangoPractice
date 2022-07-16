# Generated by Django 3.2.5 on 2022-07-16 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0005_remove_meetups_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetups',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='meetups.location'),
            preserve_default=False,
        ),
    ]
