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

    @property
    def active_version(self):
        return self.version_set.filter(is_active=True).last()


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    number = models.IntegerField(**NULLABLE, verbose_name='Номер версии')
    name = models.CharField(max_length=250, verbose_name='Название')
    is_active = models.BooleanField(default=True, verbose_name='Текущая версия')

    def __str__(self):
        return f'{self.number} - {self.name}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
