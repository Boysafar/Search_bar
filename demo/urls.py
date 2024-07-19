from django.urls import path
from demo.views import search_view

urlpatterns = [
    path('', search_view, name='search'),
]
