# TableBuilder

The goal is to build a simple backend for a table builder app, where the user can build tables dynamically. The app has the following endpoints:

## Request type - Endpoint Action

1. POST /api/table -> Generate dynamic Django model based on user provided fields types and titles. The field type can be a string, number, or Boolean. HINT: you can use Python type function to generate models on the fly and the schema editor to make schema changes just like the migrations

2. PUT /api/table/:id -> This end point allows the user to update the structure of dynamically generated model.

3. POST /api/table/:id/row -> Allows the user to add rows to the dynamically generated model while respecting the model schema

4. GET /api/table/:id/rows -> Get all the rows in the dynamically generated model Requirements:

