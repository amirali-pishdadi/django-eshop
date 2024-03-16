# Generated by Django 4.1.2 on 2023-01-15 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0007_product_brand'),
        ('account_module', '0002_alter_user_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='متن پیام')),
                ('is_read_by_admin', models.BooleanField(default=False, verbose_name='خوانده شده / نشده توسط مدیر')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_module.product', verbose_name='محصول')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'نظر',
                'verbose_name_plural': 'نظرات',
            },
        ),
    ]
