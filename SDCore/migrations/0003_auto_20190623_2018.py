# Generated by Django 2.2.2 on 2019-06-23 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SDCore', '0002_encriptedvotes'),
    ]

    operations = [
        migrations.AddField(
            model_name='electoralcort',
            name='closed_votes',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='electoralcort',
            name='private_key',
            field=models.TextField(),
        ),
    ]
