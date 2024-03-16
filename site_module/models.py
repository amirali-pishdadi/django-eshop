from django.db import models


# Create your models here.

class site_setting(models.Model):
    site_name = models.CharField(max_length=200, verbose_name='نام سایت', null=True, blank=True)
    site_url = models.CharField(max_length=200, verbose_name='دامنه سایت', null=True, blank=True)
    site_logo = models.ImageField(upload_to="images/site_module")
    email = models.EmailField(verbose_name='ایمیل', null=True, blank=True)
    address = models.CharField(verbose_name='ادرس', null=True, blank=True, max_length=200)
    about_us = models.TextField(verbose_name='درباره ما', null=True, blank=True)
    phone = models.IntegerField(verbose_name='شماره سایت', null=True, blank=True)
    copy_right = models.CharField(max_length=200, verbose_name='متن کپی رایت', null=True, blank=True)
    is_main_setting = models.BooleanField(verbose_name="تنظیمات اصلی")

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = "تنظیمات"

    def __str__(self):
        return self.site_name


class FooterLinkBoxes(models.Model):
    title = models.CharField(max_length=200, verbose_name='نام', null=True, blank=True)

    class Meta:
        verbose_name = "دسته بندی لینک های پایین صفحه"
        verbose_name_plural = "دسته بندی های لینک های پایین صفحه"

    def __str__(self):
        return self.title


class FooterLink(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True, verbose_name='نام')
    url = models.URLField(verbose_name='لینک')
    footer_link_box = models.ForeignKey(to=FooterLinkBoxes, on_delete=models.CASCADE, null=True, blank=True,
                                        verbose_name='دسته بندی')

    class Meta:
        verbose_name = 'لینک پایین صفحه'
        verbose_name_plural = 'لینک های پایین صفحه'

    def __str__(self):
        return self.title


class Slider(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام")
    url = models.URLField(max_length=500, null=True, blank=True, verbose_name='لینک')
    image = models.ImageField(upload_to='images/sliders', null=True, blank=True, verbose_name='تصویر اسلایدر')
    is_active = models.BooleanField(default=True, null=False, blank=False, verbose_name='فعال / غیرفعال')

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدر ها'

    def __str__(self):
        return self.name


class HeaderLink(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True, verbose_name='نام')
    url = models.URLField(verbose_name='لینک')

    class Meta:
        verbose_name = 'لینک سر صفحه'
        verbose_name_plural = 'لینک های سر صفحه'

    def __str__(self):
        return self.title
