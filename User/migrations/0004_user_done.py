# Generated by Django 4.2.4 on 2023-08-11 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_alter_user_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
