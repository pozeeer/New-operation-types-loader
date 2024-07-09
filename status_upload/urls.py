from django.contrib import admin
from django.urls import path

from .views import NewTypeOperation,AllTypeOperation

urlpatterns = [
    path('new_operation_types/',NewTypeOperation.as_view(),name='new_operation_types'),
    path('all_operation_types/',AllTypeOperation.as_view(),name='all_operation_types')
]
