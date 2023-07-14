from rest_framework import generics
from .models import DynamicTable
from .serializers import DynamicTableSerializer

class DynamicTableListCreateView(generics.ListCreateAPIView):
    queryset = DynamicTable.objects.all()
    serializer_class = DynamicTableSerializer

class DynamicTableUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DynamicTable.objects.all()
    serializer_class = DynamicTableSerializer

class DynamicTableRowCreateView(generics.CreateAPIView):
    queryset = DynamicTable.objects.all()
    serializer_class = DynamicTableSerializer

class DynamicTableRowListView(generics.ListAPIView):
    queryset = DynamicTable.objects.all()
    serializer_class = DynamicTableSerializer