from django.shortcuts import render
import mimetypes
import os
from django.http.response import HttpResponse
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import*
import pandas as pd
import json

# Create your views here.
class main():
    def home(request):
        item = Orders.objects.all().values()
        df = pd.DataFrame(item)
        df1 = df.drop_duplicates(subset=['id_order', 'client_name', 'client_surname', 'order_date', 'price'])
        mydict = {
            "df": df.to_html(),
            "df1": df1.to_html()
        }
        return render(request, 'index.html', context=mydict)


class pandasdemo_view(APIView):
    def get(self, request):
        item = Orders.objects.all().values()
        df = pd.DataFrame(item)
        df1 = df.drop_duplicates(subset=['id_order', 'client_name', 'client_surname', 'order_date', 'price'])
        a = df1.to_dict()
        return Response(a)
