from django.contrib import admin
from django.urls import path, include
from django.views.decorators.cache import cache_page

from homework.views import home, get_profession, human_1, add_human

urlpatterns = [
    # path('profession/<int:profession_id>/', get_profession, name='Profession'),
    # path('home/<int:human_id>/', human_1, name='Human_1'),
    # path('add_human/', add_human, name='Add_human'),
    # path('home/', home.as_view(), name='Home'),
    path('profession/<int:profession_id>/', get_profession.as_view(), name='Profession'),
    path('home/<int:pk>/', human_1.as_view(), name='Human_1'),
    path('add_human/', add_human.as_view(), name='Add_human'),
    # path('home/', home, name='Home'),
    path('home/', cache_page(30)(home), name='Home'),

]