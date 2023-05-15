from django.contrib import admin
from .models import *


# Register your models here.


class PageVisitAdmin(admin.ModelAdmin):
    list_display = ('visit', 'create_at')
    list_filter = ('create_at',)


admin.site.register(PageVisit, PageVisitAdmin)

admin.site.register(User)
admin.site.register(EmbadedVideo)
admin.site.register(Slider)
admin.site.register(ContactUs)
admin.site.register(Career)
admin.site.register(Partner)
admin.site.register(PDF)
admin.site.register(Marketing)
admin.site.register(GalleryCat)
admin.site.register(Gallery)
admin.site.register(VideoGallery)

