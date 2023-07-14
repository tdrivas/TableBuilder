from django.urls import path
from .views import *

urlpatterns = [
    path('api/table', DynamicTableCreateView.as_view(), name='dynamic-table'),
    path('api/table/<int:pk>', DynamicTableUpdateView.as_view(), name='update-dynamic-table'),
    path('api/table/<int:pk>/row', AddRowView.as_view(), name='add-dynamic-table-row'),
    path('api/table/<int:pk>/rows', GetRowsView.as_view(), name='get-dynamic-table-rows'),
]
