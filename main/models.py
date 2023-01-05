from django.db import models

class Category(models.Model):
    name = models.CharField('Название', max_length=100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    title = models.CharField('Название', max_length=60)
    desc = models.TextField('Описание', null=True, blank=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField('Обложка', upload_to='product_image', blank=True, null=True)
    date = models.DateField(auto_now=True, blank=True)
    state = models.BooleanField('Действительно?', default=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'Товар: {self.title} | Цена: {self.price} руб.'
