from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование продукта')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование продукта')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    photo = models.ImageField(upload_to='product/', **NULLABLE, verbose_name='фото')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    create_data = models.DateTimeField(**NULLABLE, verbose_name='Дата создания')
    last_change_data = models.DateTimeField(**NULLABLE, verbose_name='Дата изменения')

    def __str__(self):
        return f'{self.name}, цена за штуку {self.price}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
