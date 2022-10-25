from django.shortcuts import render
from .models import Category,Brand,Product,ProductAttributes,Banner
from django.http import JsonResponse,HttpResponse
from django.template.loader import render_to_string

# Create your views here.
def home(request):
    data = Product.objects.filter(is_featured=True).order_by('-id')
    banner = Banner.objects.all().order_by('-id')
    return render(request,'index.html',{"data":data,"banner":banner})

def Category_list(request):
    data = Category.objects.all().order_by('-id')
    return render(request,'category_list.html',{"data":data})

def Brands_list(request):
    data = Brand.objects.all().order_by('-id')
    return render(request,'brands_list.html',{"data":data})

def Product_List(request):
    data = Product.objects.all().order_by('-id')
    # category=Product.objects.distinct().values('category__title','category__id')
    # brand = Product.objects.distinct().values('brand__title',"brand__id")
    # colors=ProductAttributes.objects.distinct().values('color__title','color__id',"color__color_code")
    # sizes = ProductAttributes.objects.distinct().values('size__title','size__id')
    return render(request,'product_list.html',{
        "data":data,
        # 'category':category,
        # 'brand':brand,
        # 'colors':colors,
        # 'sizes':sizes
    })
def Category_Product_List(request,id):
    category = Category.objects.get(id=id)
    data = Product.objects.filter(category=category).order_by('-id')
    # category = Product.objects.distinct().values('category__title', 'category__id')
    # brand = Product.objects.distinct().values('brand__title', "brand__id")
    # colors = ProductAttributes.objects.distinct().values('color__title', 'color__id', "color__color_code")
    # sizes = ProductAttributes.objects.distinct().values('size__title', 'size__id')
    return render(request,'category_product_list.html',{
        'data':data,
        # 'category': category,
        # 'brand': brand,
        # 'colors': colors,
        # 'sizes': sizes
    })

def Brand_product_list(request,id):
    brand = Brand.objects.get(id=id)
    data = Product.objects.filter(brand=brand)
    # category = Product.objects.distinct().values('category__title', 'category__id')
    # brand = Product.objects.distinct().values('brand__title', "brand__id")
    # colors = ProductAttributes.objects.distinct().values('color__title', 'color__id', "color__color_code")
    # sizes = ProductAttributes.objects.distinct().values('size__title', 'size__id')
    return render(request,"brand_product_list.html",{
        'data':data,
        # 'category': category,
        # 'brand': brand,
        # 'colors': colors,
        # 'sizes': sizes
    })

# product details page
def Product_Details_page(request,slug,id):
    product = Product.objects.get(id=id)
    related_products = Product.objects.filter(category=product.category).exclude(id=id)[:3]
    return render(request,'product_details_page.html',{"data":product,"related_product":related_products})

# search function for home page
def search_products(request):
    qs=request.GET['q']
    data = Product.objects.filter(title__icontains=qs).order_by('-id')
    return render(request,'search_product.html',{'data':data})

# filter data by products
def filter_data(request):
    colors = request.GET.getlist('color[]')
    print(colors)
    categories = request.GET.getlist('category[]')
    brands = request.GET.getlist('brand[]')
    sizes = request.GET.getlist('size[]')
    minprice = request.GET['minprice']
    maxprice = request.GET['maxprice']
    allProducts=Product.objects.all().order_by('-id').distinct()
    allProducts = allProducts.filter(productattributes__price__gte=minprice)
    allProducts = allProducts.filter(productattributes__price__lte=maxprice)
    if len(colors) > 0:
        allProducts =allProducts.filter(productattributes__color_id__in=colors).distinct()
        print(allProducts)
    if len(categories) > 0:
        allProducts = allProducts.filter(category__id__in=categories).distinct()
    if len(brands) > 0:
        allProducts = allProducts.filter(brand__id__in=brands).distinct()
    if len(sizes) > 0:
        allProducts = allProducts.filter(productattributes__size_id__in=sizes).distinct()
    t = render_to_string('ajax/product_list.html', {'data': allProducts})
    # print(t)

    return JsonResponse({'data':t})