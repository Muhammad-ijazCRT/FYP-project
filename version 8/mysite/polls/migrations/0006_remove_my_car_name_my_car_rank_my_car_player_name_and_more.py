# Generated by Django 4.0.4 on 2022-05-31 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_alter_my_car_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='my_car',
            name='name',
        ),
        migrations.AddField(
            model_name='my_car',
            name='RANK',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='my_car',
            name='player_name',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='my_car',
            name='Number_of_brakes',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
