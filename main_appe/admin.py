from django.contrib import admin
from .models import Banner,Category,Brand,Color,Size,Product,ProductAttributes

# Register your models here.


class BannerAdmin(admin.ModelAdmin):
    list_display = ['id','image_tag','alt_text']
admin.site.register(Banner,BannerAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','image_get']

admin.site.register(Category,CategoryAdmin)


admin.site.register(Brand)


class ColorAdmin(admin.ModelAdmin):
    list_display = ['title','color_get']
admin.site.register(Color,ColorAdmin)

admin.site.register(Size)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title','brand','category','status','is_featured']
    list_editable = ('status',"is_featured",)

admin.site.register(Product,ProductAdmin)

class ProductAttributes_Admin(admin.ModelAdmin):
    list_display = ['id','product','image_tag','color','size','price']
admin.site.register(ProductAttributes,ProductAttributes_Admin)
