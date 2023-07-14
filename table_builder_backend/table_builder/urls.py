from django.urls import path
from .views import (
    DynamicTableListCreateView,
    DynamicTableUpdateView,
    DynamicTableRowCreateView,
    DynamicTableRowListView,
)

urlpatterns = [
    path('api/table', DynamicTableListCreateView.as_view(), name='dynamic-table'),
    path('api/table/<int:pk>', DynamicTableUpdateView.as_view(), name='update-dynamic-table'),
    path('api/table/<int:pk>/row', DynamicTableRowCreateView.as_view(), name='add-dynamic-table-row'),
    path('api/table/<int:pk>/rows', DynamicTableRowListView.as_view(), name='get-dynamic-table-rows'),
]