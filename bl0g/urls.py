from django.urls import path
from .views import *

urlpatterns = [
    path('', AppleLand.as_view(), name='home'),
    # path('', appleland, name='home'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('product/<int:mod_id>', view_mod, name='mod'),
]