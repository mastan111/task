# task

Softwares used
==============
Programming Language -> Python
restframework -> Django Rest Framework
Database --> sqlite3

Version configurations
======================
python -> 3.8.14
djangorestframework -> 3.14.0
django-import-export -> 3.0.2
pandas -> 1.5.2


API Information
===============
1.import excel data to django database using django import export library.

Endpoint: http://localhost:8000/import_excel_using_import_export/
request method: POST
request body: In request body we need to pass xlsx file with key as 'products_file' and value as file which i have attached in the project director.


2. import excel data to django database using pandas library.

Endpoint: http://localhost:8000/import_excel_using_pandas/
request method: POST
request body: In request body we need to pass xlsx file with key as 'products_file' and value as file which i have attached in the project director.


3. search api to search product by product name

Endpoint: http://localhost:8000/get_product/<str:name>/
request method: GET
Note: in the above endpoint in place of <str:name> we have to specify our product name


4. search api to search product by product name with limit response by 5 records

Endpoint: http://localhost:8000/get_products_by_post/
request method: POST
request body: in request body we have to pass product name with key as "name" and value as our product name as given below.
{
    "name":"Carrot"
}




