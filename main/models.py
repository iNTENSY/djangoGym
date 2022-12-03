from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=60)
    desc = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now=True)
    state = models.BooleanField(default=True)

    def __str__(self):
        return f'Товар: {self.title} | Price: {self.price}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
