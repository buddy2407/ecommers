from django.urls import path,include
from main_appe import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('category_list',views.Category_list,name="category_list"),
    path('brands_list',views.Brands_list,name="brands_list"),
    path('product_list',views.Product_List,name='product_list'),
    path('search_product',views.search_products,name="search_product"),

    path('category_product_list/<id>',views.Category_Product_List,name='category_product_list'),
    path('brand_product_list/<id>',views.Brand_product_list,name="brand_product_list"),
    path('product_details/<slug>/<id>',views.Product_Details_page,name='product_details'),
    path('filter_products',views.filter_data,name='filter_products'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)