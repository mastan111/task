# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FoodSales
import pandas as pd
import json


#import data by using import export

from tablib import Dataset
class Import_Excel_Using_Import_Export(APIView):
    def post(self, request, *args, **kwargs):
        dataset = Dataset()
        products = request.FILES["products_file"]
        imported_data = dataset.load(products.read(),format='xlsx')
        for data in imported_data:
            obj=FoodSales(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7]
            )
            obj.save()
        return Response({"status":"success","message":"records saved successfully"})


#import data by using pandas
class Import_Excel_Using_pandas(APIView):
    def post(self,request,*args,**kwargs): 
        products = request.FILES["products_file"]        
        empexceldata = pd.read_excel(products)        
        dbframe = empexceldata
        for dbframe in dbframe.itertuples():
            obj= FoodSales.objects.create(OrderDate=dbframe.OrderDate,Region=dbframe.Region,
                                            City=dbframe.City,Category=dbframe.Category,Product=dbframe.Product,
                                            Quantity=dbframe.Quantity,UnitPrice=dbframe.UnitPrice)
            obj.save()
        return Response({"status":"success","message":"record saved successfully"})


#Get API to search product
# http://localhost:8000/get_product/wheat/
class SearchProdcut(APIView):
    def get(self,request,name,*args,**kwargs):
        try:
            products=FoodSales.objects.filter(Product__iexact=name).values()
            return Response({"status":"success","results":products},status=200)
        except Exception as e:
            return Response({"status":"failed","message":str(e)})


#Post API to search and get first five products
# http://localhost:8000/get_products_by_post/
class SearchProdcutByPOST(APIView):
    def post(self,request,*args,**kwargs):
        data=json.loads(request.body)
        name=data.get("name")
        try:
            products=FoodSales.objects.filter(Product__iexact=name)[0:5].values()
            return Response({"status":"success","results":products},status=200)
        except Exception as e:
            return Response({"status":"failed","message":str(e)})