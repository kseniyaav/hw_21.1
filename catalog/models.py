from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    """
    Класс для создания категории продукта
    """
    name = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    """
    Класс для создания продукта
    """
    name = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    photo = models.ImageField(upload_to='product/', **NULLABLE, verbose_name='фото')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    create_data = models.DateTimeField(**NULLABLE, verbose_name='Дата создания')
    last_change_data = models.DateTimeField(**NULLABLE, verbose_name='Дата изменения')
    is_published = models.BooleanField(default=False, **NULLABLE, verbose_name='Опубликовано')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='владелец')

    def __str__(self):
        return f'{self.name}, цена за штуку {self.price}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    @property
    def active_version(self):
        return self.version_set.filter(is_active=True).last()


class Version(models.Model):
    """
    Класс для создания версии товара
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    number = models.IntegerField(**NULLABLE, verbose_name='Номер версии')
    name = models.CharField(max_length=250, verbose_name='Название')
    is_active = models.BooleanField(default=True, verbose_name='Текущая версия')

    def __str__(self):
        return f'{self.number} - {self.name}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'