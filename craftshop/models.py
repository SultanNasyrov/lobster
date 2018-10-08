from django.db import models
from django.urls import reverse


class BeerManager(models.Manager):
    """

    Beer products manager returns only objects that are available to be displayed on the site.

    """
    def get_queryset(self):
        """Return filtered be available field(True) queryset"""
        return super().get_queryset().filter(available=True)


class SnackManager(models.Manager):
    """

    Snack products manager returns only objects that are available to be displayed on the site.

    """

    def get_queryset(self):
        """Return filtered be available field(True) queryset"""
        return super().get_queryset().filter(available=True)


class Beer(models.Model):
    """Contains all info about beer instance.

    available True mean that product is displayed on the site
    best seller means that product is displayed on the index page in best sellers block

    """
    filtering_types = (
        ('f', 'Фильтрованное'),
        ('n', 'Нефильтрованное'),
    )
    image = models.FileField(upload_to='beer_images/', verbose_name='Изображение')
    available = models.BooleanField(default=True, verbose_name='ОТображается на сайте')
    best_seller = models.BooleanField(default=False, verbose_name='Выводить на главный экран')
    name = models.CharField(max_length=200, default='', verbose_name='Название')
    beer_type = models.CharField(max_length=200, default='', verbose_name='Светлое/темное')
    filtering_type = models.CharField(max_length=200, choices=filtering_types, default='f', verbose_name='Фильтрация')
    fortress = models.FloatField(default=1.0, verbose_name='Крепость(%)')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена')
    country = models.CharField(max_length=200, default='', verbose_name='Страна производитель')
    description = models.TextField(default='', verbose_name='Описание')

    display = BeerManager()

    class Meta:
        ordering = ['name']
        verbose_name = 'Пивасик'
        verbose_name_plural = 'Пивасик'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """returns absolute url for beer detail view"""
        return reverse('beer_detail', args=[str(self.id)])


class SnackCategory(models.Model):
    """Snack category model"""

    name = models.CharField(max_length=50, verbose_name='Название', default='')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name


class Snack(models.Model):
    """Contains info about snack instance

    available True mean that product is displayed on the site
    best seller means that product is displayed on the index page in best sellers block
    if product is packed means it is sold by weight, otherwise by peace

    """
    image = models.ImageField(upload_to='snacks/', verbose_name='Изображение')
    available = models.BooleanField(default=True, verbose_name='Доступен на сайте')
    best_seller = models.BooleanField(default=False, verbose_name='Выводить на главный экран')
    category = models.ForeignKey('SnackCategory', on_delete=models.DO_NOTHING)
    packed = models.BooleanField(default=False, verbose_name='На развес')
    name = models.CharField(max_length=250, default='', verbose_name='Название')
    price = models.PositiveIntegerField(default=1, verbose_name='Цена')
    description = models.TextField(default='', verbose_name='Описание')

    display = SnackManager()

    class Meta:
        ordering = ['name']
        verbose_name = 'Закуска'
        verbose_name_plural = 'Закуски'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """returns absolute url for beer detail view"""
        return reverse('snack_detail', args=[str(self.id)])


class Order(models.Model):
    """

    Order model. Created by order function inside Cart class.

    """
    name = models.CharField(max_length=500, default='', verbose_name='Имя')
    phone = models.CharField(max_length=15, default='', verbose_name='Номер телефона')
    total = models.PositiveIntegerField(default=0, verbose_name='Сумма корзины')
    executed = models.BooleanField(default=False, verbose_name='Исполнен')
    date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ ' + str(self.id)


class OrderItem(models.Model):
    """

    Order item

    """

    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    name = models.CharField(max_length=500, default='', verbose_name='Наименование продукции')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена товара')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    subtotal = models.PositiveIntegerField(default=1, verbose_name='Стоимость товара')

    def __str__(self):
        return self.name
