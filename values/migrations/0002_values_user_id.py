# Generated by Django 4.2.4 on 2023-08-13 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('values', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='values',
            name='user_id',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
    ]