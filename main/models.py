from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=60)
    desc = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_image', blank=True, null=True,)
    date = models.DateField(auto_now=True, blank=True)
    state = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'Товар: {self.title} | Price: {self.price}'
