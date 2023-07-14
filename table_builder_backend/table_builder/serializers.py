from rest_framework import serializers
from .models import DynamicTable

class DynamicTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = DynamicTable
        fields = ['field_type', 'field_title']