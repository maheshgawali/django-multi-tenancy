# Generated by Django 2.1.3 on 2018-11-17 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mt_core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dbdetails',
            name='port',
            field=models.IntegerField(),
        ),
    ]
