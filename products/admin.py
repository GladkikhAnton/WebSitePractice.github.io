from django.contrib import admin
from .models import Product, ProductImage, TypeOfProduct


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0

class TypeOfProductAdmin (admin.ModelAdmin):
    list_display = [field.name for field in TypeOfProduct._meta.fields]
    class Meta:
        model = TypeOfProduct
admin.site.register(TypeOfProduct, TypeOfProductAdmin)

class ProductAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImageInline]
    class Meta:
        model = Product
admin.site.register(Product, ProductAdmin)

class ProductImageAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]
    class Meta:
        model = ProductImage
admin.site.register(ProductImage, ProductImageAdmin)
