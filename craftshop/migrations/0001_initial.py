# Generated by Django 2.1.1 on 2018-10-07 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='beer_images/', verbose_name='Изображение')),
                ('name', models.CharField(default='', max_length=200, verbose_name='Название')),
                ('beer_type', models.CharField(default='', max_length=200, verbose_name='Светлое/темное')),
                ('filtering_type', models.CharField(default='', max_length=200, verbose_name='Фильтрация')),
                ('fortress', models.FloatField(default=1.0, verbose_name='Крепость(%)')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена')),
                ('country', models.CharField(default='', max_length=200, verbose_name='Страна производитель')),
                ('description', models.TextField(default='', verbose_name='Описание')),
                ('best_seller', models.BooleanField(default=False, verbose_name='Выводить на главный экран')),
            ],
            options={
                'verbose_name_plural': 'Пивасик',
                'verbose_name': 'Пивасик',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=500, verbose_name='Имя')),
                ('phone', models.CharField(default='', max_length=15, verbose_name='Номер телефона')),
                ('total', models.PositiveIntegerField(default=0, verbose_name='Сумма корзины')),
                ('executed', models.BooleanField(default=False, verbose_name='Исполнен')),
                ('date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Заказы',
                'verbose_name': 'Заказ',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=500, verbose_name='Наименование продукции')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена товара')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Количество')),
                ('subtotal', models.PositiveIntegerField(default=1, verbose_name='Стоимость товара')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='craftshop.Order')),
            ],
        ),
        migrations.CreateModel(
            name='SiteInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.FileField(upload_to='main/', verbose_name='Логотип')),
                ('tagline', models.CharField(default='', max_length=750, verbose_name='Слоган')),
                ('tagline_2', models.CharField(default='', max_length=500, verbose_name='Слоган 2')),
                ('banner', models.ImageField(default='', upload_to='main/', verbose_name='Баннер')),
                ('phone_number', models.CharField(default='', max_length=20, verbose_name='Номер телефона')),
                ('address', models.CharField(default='', max_length=500, verbose_name='Адрес')),
                ('insta_link', models.URLField(default='', verbose_name='Ссылка на инстаграм')),
            ],
            options={
                'verbose_name_plural': 'Главная',
                'verbose_name': 'Главная',
            },
        ),
        migrations.CreateModel(
            name='Snack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('packing', models.BooleanField(default=False, verbose_name='На развес')),
                ('image', models.ImageField(upload_to='snacks/', verbose_name='Изображение')),
                ('name', models.CharField(default='', max_length=250, verbose_name='Название')),
                ('price', models.PositiveIntegerField(default=1, verbose_name='Цена')),
                ('description', models.TextField(default='', verbose_name='Описание')),
                ('best_seller', models.BooleanField(default=False, verbose_name='Выводить на главный экран')),
            ],
            options={
                'verbose_name_plural': 'Закуски',
                'verbose_name': 'Закуска',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SnackCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name_plural': 'Категории',
                'verbose_name': 'Категория',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='snack',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='craftshop.SnackCategory'),
        ),
    ]
