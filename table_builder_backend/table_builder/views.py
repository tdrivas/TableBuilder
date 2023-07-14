from django.db import models
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.contenttypes.models import ContentType
from django.views.generic import View
from django.views.generic import UpdateView
from .models import DynamicTable
from .serializers import  DynamicTableSerializer


class DynamicTableCreateView(View):

    def get(self, request, format=None):
        # Retrieve existing dynamic tables
        dynamic_tables = DynamicTable.objects.all()

        # Serialize the dynamic tables
        serializer = DynamicTableSerializer(dynamic_tables, many=True)
        serialized_data = serializer.data

        return JsonResponse({'status': 'success', 'data': serialized_data})

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        model_name = request.POST.get('model_name')
        fields = request.POST.getlist('fields[]')

        # Create the dynamic model
        model_attrs = {
            '__module__': __name__,
            'id': models.AutoField(primary_key=True),
        }

        # Add fields to the dynamic model
        for field in fields:
            field_name, field_type = field.split(',')
            model_attrs[field_name] = models.CharField(max_length=100)

        # Create the dynamic model class
        dynamic_model = type(model_name, (models.Model,), model_attrs)

        # Create the database table for the dynamic model
        dynamic_model.objects.model._meta.db_table = model_name
        ContentType.objects.get_for_model(dynamic_model).save()

        return JsonResponse({'status': 'success', 'message': 'Dynamic model created successfully.'})



class DynamicTableUpdateView(UpdateView):
    model = DynamicTable
    fields = ['field_type', 'field_title']  # Adjust the fields as per your model

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        # Additional logic for updating the dynamic table structure if needed
        # ...

        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response

    def get_success_url(self):
        return '/api/table/' + str(self.object.pk)  # Redirect to the updated dynamic table



class AddRowView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, id, *args, **kwargs):
        # Get the dynamically generated table by its ID
        dynamic_table = DynamicTable.objects.get(id=id)

        # Process the submitted row data and add it to the dynamic table
        row_data = request.POST.get('row_data')  # Assuming the row data is submitted as a form field

        # Create a new row in the dynamic table
        dynamic_table_row = dynamic_table

        # Process the row data and assign values to corresponding fields
        for field_name, field_value in row_data.items():
            setattr(dynamic_table_row, field_name, field_value)

        # Save the dynamic table with the new row
        dynamic_table_row.save()

        return JsonResponse({'status': 'success', 'message': 'Row added successfully.'})


class GetRowsView(View):
    def get(self, request, *args, **kwargs):
        # Fetch all rows from the dynamically generated table
        dynamic_table_rows = DynamicTable.objects.all()

        # Serialize the rows
        serialized_rows = DynamicTableSerializer(dynamic_table_rows, many=True).data

        return JsonResponse({'status': 'success', 'rows': serialized_rows})
