from django.db import models
from django.contrib.auth.models import AbstractUser
from product_module.models import Product


# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(verbose_name= 'نام', max_length=150, blank=True)
    last_name = models.CharField(verbose_name= 'نام خانوادگی', max_length=150, blank=True)
    avatar = models.ImageField(upload_to='images/user_avatar', verbose_name='آواتار', null=True, blank=True)
    phone_number = models.IntegerField(verbose_name='شماره تلفن', null=True, blank=True , max_length="11")
    email_active_code = models.CharField(max_length=72, verbose_name='کد فعالسازی', null=True, blank=True)
    about_user = models.TextField(max_length=300 , verbose_name='درباره کاربر', null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True , verbose_name="آدرس")

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        if self.first_name is not '' and self.last_name is not '':
            return self.get_full_name()
        return self.email


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")
    message = models.TextField(verbose_name="متن پیام")
    parent = models.ForeignKey("Comment" , on_delete=models.CASCADE , verbose_name="والد" , null=True , blank=True)
    is_read_by_admin = models.BooleanField(default=False, verbose_name="خوانده شده / نشده توسط مدیر")
    time_create = models.DateTimeField(verbose_name="تاریخ ایجاد", auto_now_add=True)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"

