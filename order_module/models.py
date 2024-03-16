from django.db import models
from account_module.models import User
from product_module.models import Product


# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name="کاربر")
    is_paid = models.BooleanField(null=True, blank=True, verbose_name="نهایی شده / نشده")
    payment_date = models.DateField(null=True, blank=True, verbose_name="تاریخ نهایی")

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = "سبد خرید"
        verbose_name_plural = "سبد های خرید"


class OrderDetail(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name="سبد خرید")
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name="محصول")
    final_price = models.IntegerField(null=True, blank=True, verbose_name="قیمت نهایی")
    count = models.IntegerField(verbose_name="تعداد" , )

    def __str__(self):
        return self.order

    def jam(self):
        majmo = self.product.price * self.count
        return majmo

    def dicount(self):
        takhfif = (self.product.price * self.count) * (self.product.discount / 100)
        return takhfif

    def dicount_mablagh_pardakht(self):
        takhfif = (self.product.price * self.count) - ((self.product.price * self.count) * self.product.discount / 100)
        return takhfif

    class Meta:
        verbose_name = "جزییات سبد خرید"
        verbose_name_plural = "جزییات سبد های خرید"
