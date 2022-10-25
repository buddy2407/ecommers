from .models import Product,ProductAttributes
from django.db.models import Min,Max
def get_fillter(request):
    category = Product.objects.distinct().values('category__title', 'category__id')
    brand = Product.objects.distinct().values('brand__title', "brand__id")
    colors = ProductAttributes.objects.distinct().values('color__title', 'color__id', "color__color_code")
    sizes = ProductAttributes.objects.distinct().values('size__title', 'size__id')
    minMaxPrice = ProductAttributes.objects.aggregate(Min('price'),Max('price'))
    data = {
        'category': category,
        'brand': brand,
        'colors': colors,
        'sizes': sizes,
        'minMaxPrice':minMaxPrice
    }
    return data