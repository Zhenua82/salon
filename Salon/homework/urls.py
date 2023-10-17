from django.contrib import admin
from django.urls import path, include
from django.views.decorators.cache import cache_page

from homework.views import home, get_profession, human_1, add_review, register, user_login, user_logout, review

urlpatterns = [
    # path('profession/<int:profession_id>/', get_profession, name='Profession'),
    # path('home/<int:human_id>/', human_1, name='Human_1'),
    # path('add_human/', add_human, name='Add_human'),
    # path('home/', home.as_view(), name='Home'),
    path('profession/<int:profession_id>/', cache_page(600)(get_profession.as_view()), name='Profession'),
    path('home/<int:pk>/', cache_page(600)(human_1.as_view()), name='Human_1'),
    path('add_review/', add_review.as_view(), name='Add_review'),
    # path('home/', home, name='Home'),
    path('', cache_page(600)(home), name='Home'),

    path('register', register, name='Register'),
    path('login', user_login, name='Login'),
    path('logout/', user_logout, name='Logout'),
    path('review', review.as_view(), name='Review'),

]
