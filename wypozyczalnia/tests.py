from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User



# Create your tests here.



class MyTest(TestCase):
    def test_something(self):
        client = Client()
        response = client.post('/wypozyczalnia/my_register',data={"username": "test", "password": "haslo"})
        request = response.wsgi_request
        assert response.status_code == 200
        user = User.objects.get(username='test')
        assert user.username == 'test'

        #raise ValueError(response)
        #params = {'username':'BaczekSraczek','password':'haslomaslo'}
        #print(request.body)
        #url = 'http://70.34.252.140:8081/wypozyczalnia/my_register'
        #r = requests.post(url=url,json=params)
