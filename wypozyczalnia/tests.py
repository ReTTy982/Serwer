from django.test import TestCase
from django.test.client import RequestFactory
import requests

# Create your tests here.



class MyTest(TestCase):
    def test_something(self):
        self.factory = RequestFactory()
        params = {'username':'BaczekSraczek','password':'haslomaslo'}
        request = self.factory.post('/wypozyczalnia/my_register',params)
        print(request)
        #url = 'http://70.34.252.140:8081/wypozyczalnia/my_register'
        #r = requests.post(url=url,json=params)
