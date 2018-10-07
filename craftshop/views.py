from django.shortcuts import render, get_object_or_404
from .models import Beer, Snack, SnackCategory


def index(request):
    beers = Beer.objects.filter(best_seller=True)[:10]
    snacks = Snack.objects.filter(best_seller=True)[:10]
    context = {
        'beers': beers,
        'snacks': snacks,
    }
    return render(request, 'index.html', context)


def beer_page(request):

    beers = Beer.objects.all()
    type = 'beer'

    context = {
        'products': beers,
        'type': type,
    }
    return render(request, 'catalog.html', context)


def snacks_page(request):

    snacks = Snack.objects.all()
    categories = SnackCategory.objects.all()
    type = 'snaks'

    context = {
        'products': snacks,
        'type': type,
        'categories': categories,
    }
    return render(request, 'catalog.html', context)


def snack_category(request, id):

    target = SnackCategory.objects.get(id=id).name
    snacks = Snack.objects.filter(category=id)
    categories = SnackCategory.objects.all()
    type = 'snaks'

    context = {
        'products': snacks,
        'type': type,
        'categories': categories,
    }
    return render(request, 'catalog.html', context)


def delivery(request):

    context = {
    }

    return render(request, 'delivery.html', context)


def about(request):


    context = {

    }
    return render(request, 'about.html', context)


def beer_detail(request, id):

    type = 'beer'
    product = get_object_or_404(Beer, id=id)

    context = {
        'type': type,
        'product': product,
    }
    return render(request, 'detail.html', context)


def snack_detail(request, id):

    type = 'snack'
    product = get_object_or_404(Snack, id=id)

    context = {

        'type': type,
        'product': product,
    }

    return render(request, 'detail.html', context)

