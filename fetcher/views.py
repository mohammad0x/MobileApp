from asyncore import write
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json
import csv
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import ItemSerializer
from django.conf import settings
import os
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@api_view(['GET'])
def items(request):
    data = []
    try:
        with open('static/data.csv',encoding='utf-8') as csvf:
            csvReader = csv.DictReader(csvf)
            for index,rows in enumerate(csvReader):
                data.append(rows)
        serializer = ItemSerializer(data,many=True)
        if len(data)>0:
            return JsonResponse({'data':serializer.data},status=200)
        else:
            return JsonResponse({'data':'no data'},status=404)
    except Exception as e:
        return JsonResponse({
            'data': 'server error'
        },status=500)

@api_view(['GET'])
def item(request,row):
    data=[]
    try:
        with open('static/data.csv',encoding='utf-8') as csvf:
            csvReader = csv.DictReader(csvf)
            for index,rows in enumerate(csvReader):
                data.append(rows)
        serializer = ItemSerializer(data[row])
        if len(data)>0:
            return JsonResponse({'data':serializer.data})
        else:
            return JsonResponse({'data':'no data'})
    except Exception as e:
        return JsonResponse({'data':'error'})
@csrf_exempt
@api_view(["POST"])
def addItem(request):
    headersCSV = ['title','description','image']      
    data=[]
    item = ItemSerializer(data = request.data)
    try:
        if item.is_valid():
            with open('static/data.csv','a',encoding='utf-8') as csvf:
                new_row = csv.DictWriter(csvf, fieldnames=headersCSV)
                new_row.writerow(request.data)
                return JsonResponse({'data':'row appended'},status=201)
        else:
            messages = item.errors
            return JsonResponse({
                data:"title and image is required"
            },status=400)
    except Exception as e:
        print(str(e))
        return JsonResponse({'data':str(e)},status=400)
@csrf_exempt
@api_view(["DELETE"])
def deleteRow(request,rowId):
    try:
        lines = list()
        with open('static/data.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
        dropped = lines.pop(rowId)
        print(lines)
        with open('static/data.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)

        return JsonResponse({
                "message":"row deleted succesfully"
            },status=202)

    except Exception as e:
       return JsonResponse({
           'data':str(e)
       },status=400)

