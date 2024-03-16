from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.text import slugify


class ProductBrand(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام برند")
    slug = models.SlugField()
    # URL field
    is_active = models.BooleanField(default=True, verbose_name="فعال شده / نشده")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "برند محصول"
        verbose_name_plural = "برند های محصول"


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='نام')
    image = models.ImageField(upload_to='images/product_module/', verbose_name='تصویر')
    price = models.IntegerField(verbose_name='قیمت')
    discount = models.IntegerField(verbose_name='تخفیف')
    quantity = models.IntegerField(verbose_name='تعداد')
    short_description = models.CharField(max_length=150, verbose_name='توضیحات کوتاه')
    brand = models.ForeignKey(to=ProductBrand, on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField(default="", unique=True)
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')
    is_delete = models.BooleanField(default=False, verbose_name="حذف شده / نشده")

    def get_absolute_url(self):
        return reverse("product-detail", args=[self.slug])

    def __str__(self):
        return f"{self.name} {self.is_active}"

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"


class ImagesProduct(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name="محصول")
    image = models.ImageField(upload_to='images/product_module', verbose_name='تصویر', blank=True)

    def __str__(self):
        return f"{self.product}"

    class Meta:
        verbose_name = "عکس محصول"
        verbose_name_plural = "عکس های محصول"


class AboutProduct(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='تیتر', max_length=80)
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to="images/product_module/about_product", verbose_name="عکس")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "نقد و بررسی محصول"
        verbose_name_plural = "نقد و بررسی محصولات"
