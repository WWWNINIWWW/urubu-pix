# Generated by Django 4.2.4 on 2023-08-11 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='done',
        ),
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=models.UUIDField(default=1),
            preserve_default=False,
        ),
    ]
