# Generated by Django 2.2.12 on 2021-11-02 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20211101_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_car',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
