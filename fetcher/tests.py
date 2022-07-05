from django.test import TestCase , Client
from rest_framework.test import RequestsClient
import json
# import urllib, json
from urllib.request import urlopen
from django.http import JsonResponse

class test_add(TestCase):

    #test invalid title
    def test_invalid_title_post(self):
        client = RequestsClient()
        response = client.post('http://127.0.0.1:8001/add_item',{'title':'','description':'helloali','image':'xx.jpg'})
        assert response.status_code == 400

    #test invalid description
    def test_invalid_description_post(self):
        client = RequestsClient()
        response = client.post('http://127.0.0.1:8001/add_item',{'title':'test','description':'','image':'xx.jpg'})
        assert response.status_code == 201

    #test invalid image
    def test_invalid_image_post(self):
        client = RequestsClient()
        response = client.post('http://127.0.0.1:8001/add_item',{'title':'test','description':'test','image':''})
        assert response.status_code == 400

     #test valid data
    def test_valid_post(self):
        client = RequestsClient()
        response = client.post('http://127.0.0.1:8001/add_item',{'title':'test','description':'test','image':'test'})
        assert response.status_code == 201


class test_valid_id_delete(TestCase):
    #test valid id
    def test_delet_post(self):
        client = RequestsClient()
        response = client.delete('http://127.0.0.1:8001/delete_row/1')
        assert response.status_code == 202
    #test invalid id
    def test_invalid_id_delete(self):
        client = RequestsClient()
        response = client.delete('http://127.0.0.1:8001/delete_row/1000')
        assert response.status_code == 400

class test_get_items(TestCase):
    #test items exist
    def test_invalid_id_delete(self):
        url = "http://127.0.0.1:8000/items"
        response = urlopen(url)
        try:
            data_json = json.loads(response.read())
        except ValueError as err:
            return JsonResponse({'status':400})
        return JsonResponse({'status':200})
