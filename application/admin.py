from django.contrib import admin
from .models import *


# Register your models here.
class ApplicationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}
    list_display = ('name', 'create_at', 'update_at')
    list_filter = ('name', 'create_at', 'update_at')


admin.site.register(Application, ApplicationAdmin)


class ApplicationCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}
    list_display = ('name', 'create_at', 'update_at')
    list_filter = ('name', 'create_at', 'update_at')


admin.site.register(ApplicationCategory, ApplicationCategoryAdmin)


class ApplicationSubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}
    list_display = ('name', 'create_at', 'update_at')
    list_filter = ('name', 'create_at', 'update_at')


admin.site.register(ApplicationSubCategory, ApplicationSubCategoryAdmin)
admin.site.register(ApplicationRequest)
