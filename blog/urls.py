from django.urls import path
from . import views

urlpatterns = [
    path('', views.EntryDetail.as_view(), name='entry_detail'),
]
