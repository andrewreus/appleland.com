from django.db import models
from django.urls import reverse

class Mod(models.Model):
    name = models.CharField(max_length=150, verbose_name='name')
    characteristics = models.TextField(blank=True, verbose_name='characteristics')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')
    image = models.ImageField(upload_to='Mod/image', verbose_name='image')
    category = models.ForeignKey("categories", on_delete=models.PROTECT, null=True)
    price = models.IntegerField(null=True, verbose_name='price')

    def get_absolute_url(self):
        return reverse('mod', kwargs={'mod_id': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class Categories(models.Model):
    name = models.CharField(max_length=150, db_index=True, verbose_name='name of categories')

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = []

