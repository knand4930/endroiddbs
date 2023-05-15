from django.contrib import admin
from .models import *


# Register your models here.

class SoftwareCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}
    list_display = ('name', 'create_at', 'update_at')
    list_filter = ('name', 'create_at', 'update_at')


admin.site.register(SoftwareCategory, SoftwareCategoryAdmin)

admin.site.register(SoftwareBlock)


class SoftwareSubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}
    list_display = ('name', 'category', 'create_at', 'update_at')
    list_filter = ('name', 'category', 'create_at', 'update_at')


admin.site.register(SoftwareSubCategory, SoftwareSubCategoryAdmin)


class SoftwareAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}
    list_display = ('name', 'category', 'create_at', 'update_at')
    list_filter = ('name', 'category', 'create_at', 'update_at')


admin.site.register(Software, SoftwareAdmin)
