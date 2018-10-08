from django.shortcuts import render, get_object_or_404
from .models import Beer, Snack, SnackCategory


def index(request):
    """Index view function returns index template with beer and snacks best sellers in context"""
    beers = Beer.display.filter(best_seller=True)[:10]
    snacks = Snack.display.filter(best_seller=True)[:10]
    context = {
        'beers': beers,
        'snacks': snacks,
    }
    return render(request, 'index.html', context)


def beer_page(request):
    """Return rendered catalog page with all beer available"""
    beers = Beer.display.all()
    type = 'beer'

    context = {
        'products': beers,
        'type': type,
    }
    return render(request, 'catalog.html', context)


def snacks_page(request):
    """Returns rendered catalog with all snacks available"""
    snacks = Snack.display.all()
    categories = SnackCategory.objects.all()
    type = 'snacks'

    context = {
        'products': snacks,
        'type': type,
        'categories': categories,
    }
    return render(request, 'catalog.html', context)


def snack_category(request, id):
    """Lists snacks by target category and returns rendered catalog template"""
    target = SnackCategory.objects.get(id=id).name
    snacks = Snack.display.filter(category=id)
    categories = SnackCategory.objects.all()
    type = 'snacks'
    context = {
        'products': snacks,
        'type': type,
        'categories': categories,
    }
    return render(request, 'catalog.html', context)


def delivery(request):
    """Delivery info page view function returns rendered delivery template"""
    return render(request, 'delivery.html')


def about(request):
    """About us page function returns rendered about template"""
    return render(request, 'about.html')


def beer_detail(request, id):
    """Returns rendered beer page. If beer is not found raises 404"""
    type = 'beer'
    product = get_object_or_404(Beer, id=id)
    context = {
        'type': type,
        'product': product,
    }
    return render(request, 'detail.html', context)


def snack_detail(request, id):
    """Returns rendered snack page. If snack is not found raises 404"""
    type = 'snack'
    product = get_object_or_404(Snack, id=id)
    context = {
        'type': type,
        'product': product,
    }
    return render(request, 'detail.html', context)

