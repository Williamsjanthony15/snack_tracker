
from django.urls import path
from django.urls.resolvers import URLPattern
from .views import SnackListView, SnackDetailView

urlpatterns = [
    path('', SnackListView.as_view(), name = 'list'),
    path('snack_detail', SnackDetailView.as_view(), name = 'details'),
]