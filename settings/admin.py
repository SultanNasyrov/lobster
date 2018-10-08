from django.contrib import admin
from .models import SiteInfo, SEO


@admin.register(SiteInfo)
class SiteInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(SEO)
class SeoAdmin(admin.ModelAdmin):
    pass
