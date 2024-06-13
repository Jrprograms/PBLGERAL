from django.test import TestCase
from django.test.client import Client 
from django.urls import reverse
from community_app.models import Community, New
from datetime import date

class CommunityIntegrationTestCase(TestCase):
    def setUp(self):
        self.client = Client() #
        Community.objects.create(
            title='Comunidade Ecodm',
            category='Comunidade',
            foundation_date='09/05/2004',
            begin_visit_time=datetime(),  
            end_visit_time=datetime(),
            longitude = '4321',
            latitude = '1234',
            link = 'http://example-Community.com',

        )
    
    def test_create_community_via_post(self):
        url = reverse('create_community_view')
        response = self.client.post(url, {
            'title'='Comunidade Ecodm',
            'category'='Comunidade',
            'foundation_date'='09/05/2004',
            'begin_visit_time'=datetime(),  
            'end_visit_time'=datetime(),
            'longitude' = '4321',
            'latitude' = '1234',
            'link' = 'http://example-Community.com',

        })

class NewIntegrationTestCase(TestCase):
    def setUp(self):
        self.client = Client() #
        New.objects.create(
            title='New de Teste',
            news_text='Texto da New de teste',
            publish_date=date.today(),
            category='Comunidade', 
            link='http://example-New.com',  

        )
    
    def test_create_new_via_post(self):
        url = reverse('create_news_view')
        response = self.client.post(url, {
            'title'='New de Teste',
            'news_text'='Texto da New de teste',
            'publish_date'=date.today(),
            'category'='Comunidade', 
            'link'='http://example-New.com', 
        })