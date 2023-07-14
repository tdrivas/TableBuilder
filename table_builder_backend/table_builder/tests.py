from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import DynamicTable


class DynamicTableAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_dynamic_table(self):
        # Test creating a dynamic table
        data = {
            "field_type": ["string", "number", "boolean"],
            "field_title": ["Name", "Age", "Active"]
        }
        response = self.client.post('/api/table', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(DynamicTable.objects.count(), 1)
        self.assertEqual(DynamicTable.objects.get().field_type, data["field_type"])
        self.assertEqual(DynamicTable.objects.get().field_title, data["field_title"])

    def test_update_dynamic_table(self):
        # Test updating the structure of a dynamic table
        dynamic_table = DynamicTable.objects.create(field_type=["string", "number"], field_title=["Name", "Age"])
        data = {
            "field_type": ["string", "number", "boolean"],
            "field_title": ["Name", "Age", "Active"]
        }
        response = self.client.put(f'/api/table/{dynamic_table.id}', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(DynamicTable.objects.get().field_type, data["field_type"])
        self.assertEqual(DynamicTable.objects.get().field_title, data["field_title"])

    def test_add_dynamic_table_row(self):
        # Test adding a row to a dynamic table
        dynamic_table = DynamicTable.objects.create(field_type=["string", "number"], field_title=["Name", "Age"])
        data = {
            "Name": "John",
            "Age": 25
        }
        response = self.client.post(f'/api/table/{dynamic_table.id}/row', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(dynamic_table.rows.count(), 1)
        self.assertEqual(dynamic_table.rows.first().data, data)

    def test_get_dynamic_table_rows(self):
        # Test retrieving all rows from a dynamic table
        dynamic_table = DynamicTable.objects.create(field_type=["string", "number"], field_title=["Name", "Age"])
        dynamic_table.rows.create(data={"Name": "Bruce Wayne", "Age": 25})
        dynamic_table.rows.create(data={"Name": "Tony Stark", "Age": 30})

        response = self.client.get(f'/api/table/{dynamic_table.id}/rows')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["data"]["Name"], "Tony Stark")
        self.assertEqual(response.data[1]["data"]["Age"], 30)
