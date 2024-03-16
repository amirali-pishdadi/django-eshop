from django.db import models


# Create your models here.

class Ads(models.Model):
    name = models.CharField(max_length=150, verbose_name='نام')
    image = models.ImageField(upload_to="images/advertisement")
    is_active = models.BooleanField(verbose_name="فعال / غیر فعال", default=True)
    url = models.URLField(verbose_name='آدرس', default='http://127.0.0.1:8000/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "تبلیغ"
        verbose_name_plural = "تبلیغات"
