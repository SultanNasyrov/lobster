from django.urls import path, re_path
from .views import (index, beer_page, snacks_page, delivery,
                    about, beer_detail, snack_detail, snack_category)

urlpatterns = [
    path('', index, name='index'),
    path('beer', beer_page, name='beer'),
    path('snacks', snacks_page, name='snacks'),
    path('snacks/category/<int:id>', snack_category, name='snacks-category'),
    path('beer/<int:id>', beer_detail, name='beer_detail'),
    path('snack/<int:id>', snack_detail, name='snack_detail'),
    path('delivery', delivery, name='delivery'),
    path('about', about, name='about'),
]
