from django.contrib import admin

from apps.product.models import Category, Product, Provider
from apps.product.models.product import UnitSizeProduct
from billing.admin import TechFactSite


# Register your models here.

@admin.register(Category, site=TechFactSite)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    search_fields = list_display
    list_filter = list_display
    fields = (("name", "description",),)




@admin.register(Product, site=TechFactSite)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["code", "provider_code", "name", "stock", "provider", ]
    search_fields = list_display
    list_filter = list_display
    list_editable = list_display[1:]
    fieldsets = (
        ("Producto", {"fields": (
            ("code", "name", "stock"),
            ("cost", "price1", "price2"),
            ("price3", "discount"),
            ("unit_size", "category",)), },),
        ("Proveedor", {"fields": ("provider_code", "provider"), },)
        ,)



@admin.register(Provider, site=TechFactSite)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ["name", "ruc", "email", "phone", ]
    search_fields = list_display
    list_filter = list_display
    list_editable = list_display[1:]
    fields = ( ("name", "ruc", "email"), ("phone", "address",))


@admin.register(UnitSizeProduct, site=TechFactSite)
class UnitSizeProductAdmin(admin.ModelAdmin):
    list_display = ["name",]
    search_fields = list_display
    list_filter = list_display
    list_editable = list_display[1:]
