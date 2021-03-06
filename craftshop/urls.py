from django.urls import path
from .views import (index, beer_page, snacks_page, delivery,
                    about, beer_detail, snack_detail)

urlpatterns = [
    path('', index, name='index'),
    path('beer', beer_page, name='beer'),
    path('snacks', snacks_page, name='snacks'),
    path('beer/<int:id>', beer_detail, name='beer_detail'),
    path('snack/<int:id>', snack_detail, name='snack_detail'),
    path('delivery', delivery, name='delivery'),
    path('about', about, name='about'),
]
