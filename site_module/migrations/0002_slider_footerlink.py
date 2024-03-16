# Generated by Django 4.1.2 on 2022-12-17 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, max_length=500, null=True, verbose_name='لینک')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/sliders', verbose_name='تصویر اسلایدر')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال / غیرفعال')),
            ],
            options={
                'verbose_name': 'اسلایدر',
                'verbose_name_plural': 'اسلایدر ها',
            },
        ),
        migrations.CreateModel(
            name='FooterLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='نام')),
                ('url', models.URLField(verbose_name='لینک')),
                ('footer_link_box', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='site_module.footerlinkboxes', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'لینک پایین صفحه',
                'verbose_name_plural': 'لینک های پایین صفحه',
            },
        ),
    ]
