from django.db import models


class SiteInfo(models.Model):
    """
    Model for base site info such as logo tagline etc.
    """

    logo = models.FileField(upload_to='main/', verbose_name='Логотип')
    tagline = models.CharField(max_length=750, verbose_name='Слоган', default='')
    tagline_2 = models.CharField(max_length=500, verbose_name='Слоган 2', default='')
    banner = models.ImageField(upload_to='main/', verbose_name='Баннер', default='')
    phone_number = models.CharField(max_length=20, default='', verbose_name='Номер телефона')
    address = models.CharField(max_length=500, default='', verbose_name='Адрес')
    insta_link = models.URLField(default='', verbose_name='Ссылка на инстаграм')

    class Meta:
        verbose_name = 'Главная'
        verbose_name_plural = 'Главная'

    def __str__(self):
        return 'Настройки сайта'


class SEO(models.Model):
    pass
