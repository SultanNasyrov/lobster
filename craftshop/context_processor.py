from settings.models import SiteInfo


def info(request):
    if SiteInfo.objects.count() > 0:
        info = SiteInfo.objects.get()
    else:
        info = {}
    return {'info': info}