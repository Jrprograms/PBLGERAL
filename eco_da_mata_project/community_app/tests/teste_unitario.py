from django.test import TestCase
from community_app.models import Community, New
from datetime import datetime
#from faker import Faker 


class NewsTestCase(TestCase)
    def setUp(self):
        fake = Faker()
        New.objects.create(
            title='New de Teste',
            news_text='Texto da New de teste',
            publish_date=date.today(),
            category='Comunidade', 
            link='http://example-New.com',       
    )

    def test_title_new(self):
        new = New.objects.get(nome='New de Teste')
        self.assertNotEqual(new.title, '')
        self.assertIsNotNone(new.title)    

    def test_text_new(self):
        new = New.objects.get(nome='New de Teste') 
        self.assertEqual(new.news_text, 'Texto da New de teste') #conferindo texto é o texto salvo no DB

    def test_publish_date_new(self):
        new = New.objects.get(nome='New de Teste')
        self.assertEqual(new.publish_date, '') #conferindo data de realização

    def test_category_new(self):
        new = New.objects.get(nome='New de Teste')
        self.assertIn(new.category, ['Ponto Turístico', 'Comunidade']) #conferindo categoria

    def test_link_new(self):
        community = Community.objects.get(nome='Comunidade de Econdm')
        self.assertAlmostEqual(community.category, ['Ponto Turístico', 'Comunidade'])


class CommunityTestCase(TestCase) 
    def setUp(self):
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

    def test_title_community(self):
        community = Community.objects.get(nome='Comunidade Ecodm')
        self.assertNotEqual(community.title, '')
        self.assertIsNotNone(community.title)

    def test_category_community(self):
        community = Community.objects.get(nome='Comunidade Ecodm')
        self.assertInEqual(community.category, ['Ponto Turístico', 'Comunidade'])

    def test_foundation_date_community(self):
        community = Community.objects.get(nome='Comunidade Ecodm') 
        self.assertEqual(community.foundation_date, '09/05/2004') #conferindo texto é o texto salvo no DB

    def test_begin_visit_time_bigger_end_visit_time_community(self):
        community = Community.objects.get(nome='Comunidade Ecodm')
        self.assertGreaterEqual(community.begin_visit_time, community.end_visit_time) #conferindo se fim > ou = inicio = True

    def test_longitude_community(self):
        community = Community.objects.get(nome='Comunidade Ecodm')
        self.assertEqual(community.latitude, '1234') 

    def test_latitude_community(self):
        community = Community.objects.get(nome='Comunidade Ecodm')
        self.assertEqual(community.longitude, '4321')

    def test_link_community(self):
        community = Community.objects.get(nome='Comunidade de Econdm')
        self.assertEqual(community.link, 'http://example-Community.com')

    