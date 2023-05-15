from django.contrib import admin
from .models import *


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}
    list_display = ('name', 'create_at', 'update_at')
    list_filter = ('name', 'create_at', 'update_at')


admin.site.register(Category, CategoryAdmin)


class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}
    list_display = ('name', 'category', 'create_at', 'update_at')
    list_filter = ('name', 'category', 'create_at', 'update_at')


admin.site.register(SubCategory, SubCategoryAdmin)


class MicroCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}
    list_display = ('name', 'subcat', 'create_at', 'update_at')
    list_filter = ('name', 'subcat', 'create_at', 'update_at')


admin.site.register(MicroCategory, MicroCategoryAdmin)


class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}
    list_display = ('title', 'price', 'create_at', 'update_at','category', 'sub_category', 'micro_category')
    list_filter = ('title', 'price', 'create_at', 'update_at')


admin.site.register(Products, ProductsAdmin)
admin.site.register(ProductRequest)
