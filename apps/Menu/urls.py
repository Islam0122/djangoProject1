from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.Menu.Category.views import DishCategoryViewSet, DrinkCategoryViewSet
from apps.Menu.Dish.views import DishModelViewSet
from apps.Menu.Drink.views import DrinkModelViewSet

dish_category_list = DishCategoryViewSet.as_view({'get': 'list',})
dish_category_detail = DishCategoryViewSet.as_view({'get': 'retrieve',})

drink_category_list = DrinkCategoryViewSet.as_view({'get': 'list',})
drink_category_detail = DrinkCategoryViewSet.as_view({'get': 'retrieve',})

dish_list = DishModelViewSet.as_view({'get': 'list',})
dish_detail = DishModelViewSet.as_view({'get': 'retrieve',})

drink_list = DrinkModelViewSet.as_view({'get': 'list',})
drink_detail = DrinkModelViewSet.as_view({'get': 'retrieve',})

urlpatterns = [
    path('dish-categories/', dish_category_list, name='dish-category-list'),
    path('dish-categories/<int:pk>/', dish_category_detail, name='dish-category-detail'),

    path('drink-categories/', drink_category_list, name='drink-category-list'),
    path('drink-categories/<int:pk>/', drink_category_detail, name='drink-category-detail'),

    path('dishes/', dish_list, name='dish-list'),
    path('dishes/<int:pk>/', dish_detail, name='dish-detail'),

    path('drinks/', drink_list, name='drink-list'),
    path('drinks/<int:pk>/', drink_detail, name='drink-detail'),
]


