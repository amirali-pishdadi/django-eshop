# Generated by Django 4.1.2 on 2023-01-15 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0004_alter_aboutproduct_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام برند')),
                ('slug', models.SlugField()),
                ('product', models.ManyToManyField(to='product_module.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'برند محصول',
                'verbose_name_plural': 'برند های محصول',
            },
        ),
    ]