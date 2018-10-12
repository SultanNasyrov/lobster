from django.db import models


class SiteInfo(models.Model):
    """
    Model for base site info such as logo tagline etc.
    """

    logo = models.FileField(upload_to='main/', verbose_name='Логотип')
    logo_text1 = models.CharField(max_length=250, default='', verbose_name='Текст лого 1',
                                  help_text='Верхняя строчка текста в логотипе')
    logo_text2 = models.CharField(max_length=250, default='', verbose_name='Текст лого 2',
                                  help_text='Нижняя строчка текста в логотипе')
    tagline = models.CharField(max_length=750, verbose_name='Заголовок(h1)', default='')
    tagline_2 = models.CharField(max_length=500, verbose_name='Заголовок(h2)', default='')
    banner = models.ImageField(upload_to='main/', verbose_name='Баннер', default='')
    phone_number = models.CharField(max_length=20, default='', verbose_name='Номер телефона')
    address = models.CharField(max_length=500, default='', verbose_name='Адрес')
    insta_link = models.URLField(default='', verbose_name='Ссылка на инстаграм')
    map = models.TextField(default='', verbose_name='Html код карты(embed)')

    class Meta:
        verbose_name = 'Главная'
        verbose_name_plural = 'Главная'

    def __str__(self):
        return 'Настройки сайта'


class SEO(models.Model):
    """

    Seo model. Contains all title and description tags content on the site

    """
    index_title = models.CharField(max_length=500, default='', verbose_name='title главной страницы')
    index_desc = models.CharField(max_length=500, default='', verbose_name='description главной страницы')
    beer_title = models.CharField(max_length=500, default='', verbose_name='title страницы пива')
    beer_desc = models.CharField(max_length=500, default='', verbose_name='description тсраницы пива')
    snacks_title = models.CharField(max_length=500, default='', verbose_name='title страницы снеков')
    snacks_desc = models.CharField(max_length=500, default='', verbose_name='description страницы снеков')
    detail_title = models.CharField(max_length=500, default='', verbose_name='title страницы товара')
    detail_desc = models.CharField(max_length=500, default='', verbose_name='description страницы товара')
    delivery_title = models.CharField(max_length=500, default='', verbose_name='title страницы доставки')
    delivery_desc = models.CharField(max_length=500, default='', verbose_name='description страницы доставки')
    about_title = models.CharField(max_length=500, default='', verbose_name='title о нас')
    about_desc = models.CharField(max_length=500, default='', verbose_name='description о нас')
    cart_title = models.CharField(max_length=500, default='', verbose_name='title страницы корзина')
    cart_desc = models.CharField(max_length=500, default='', verbose_name='description страницы корзина')

    class Meta:
        verbose_name = 'Настройки SEO'
        verbose_name_plural = 'Настройки SEO'

    def __str__(self):
        return 'Настройки SEO'


