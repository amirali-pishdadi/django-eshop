# Generated by Django 4.2 on 2023-06-13 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0014_alter_user_first_name_alter_user_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='آدرس'),
        ),
    ]
