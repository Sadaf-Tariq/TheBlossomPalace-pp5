from django.contrib import admin
from .models import Type, FlowerCount, Product, Rating

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'flower_type',
        'price',
        'rating',
        'featured_image',
        'flower_count',
    )

    ordering = ('sku',)

class TypeAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(FlowerCount)
admin.site.register(Rating)