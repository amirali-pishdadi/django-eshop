# Generated by Django 4.1.2 on 2023-04-06 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0013_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='نام خانوادگی'),
        ),
    ]
