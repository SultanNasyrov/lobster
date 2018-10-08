from .models import SiteInfo, SEO


def info(request):
    """returns first objects that contains all site info and setting"""
    if SiteInfo.objects.count() > 0:
        info = SiteInfo.objects.get()
    else:
        info = {}
    return {'info': info}


def seo(request):
    """returns seo model instance"""
    if SEO.objects.count() > 0:
        seo = SEO.objects.get()
    else:
        seo = {}
    return {'seo': seo}