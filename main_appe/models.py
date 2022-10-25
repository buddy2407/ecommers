from django.db import models
from django.utils.html import mark_safe

# Create your models here.

class Banner(models.Model):
    image=models.ImageField(upload_to='banner_images')
    alt_text=models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = '1. Banners'

    def __str__(self):
        return self.alt_text
    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />'%(self.image.url))

class Category(models.Model):
    title=models.CharField(max_length=300)
    image=models.ImageField(upload_to='category_images')

    class Meta:
        verbose_name_plural = '2. Categorys'

    def __str__(self):
        return self.title
    def image_get(self):
        return mark_safe('<img src="%s" width="80" />'%(self.image.url))

class Brand(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='brand_images')

    class Meta:
        verbose_name_plural = '3. Brands'

    def __str__(self):
        return self.title

class Color(models.Model):
    title=models.CharField(max_length=100)
    color_code=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = '4. Colors'

    def color_get(self):
        return mark_safe('<div style="width:20px;height:20px; background:%s"></div>' % (self.color_code))

    def __str__(self):
        return self.title

class Size(models.Model):
    title=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = '5. Sizes'

    def __str__(self):
        return self.title


class Product(models.Model):
    title=models.CharField(max_length=300)
    slug=models.CharField(max_length=300)
    detail=models.TextField()
    specs=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    status=models.BooleanField(default=True)
    is_featured=models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = '6. Products'

    def __str__(self):
        return self.title

class ProductAttributes(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    color=models.ForeignKey(Color,on_delete=models.CASCADE)
    size=models.ForeignKey(Size,on_delete=models.CASCADE)
    price=models.PositiveIntegerField(default=0)
    image=models.ImageField(upload_to='product_images',null=True)

    class Meta:
        verbose_name_plural = '7. ProductAttributes'

    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' % (self.image.url))

    def __str__(self):
        return self.product.title


