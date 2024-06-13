from django.test import TestCase
from Community.models import Evento
from datetime import datet
from faker import Faker 
import uuid

class NewsTestCase(TestCase)
    def setUp(self):
        fake = Faker()
        New.objects.create(
            id=fake.uuid4(),
            id_community=fake.random_int(min=1, max=10),
            title='New de Teste'
            news_text='Texto da New de teste'
            publish_date=date.today()
            category='Comunidade' 
            link='http://example.com'       
    )

    def test_new_criada_com_sucesso(self):
        community = New.objects.get(nome='New de Teste') 
        self.assertEqual(new.title, 'Texto da Notícia') #conferindo texto

    def test_new_da_community(self):
        community = Community.objects.get(nome='New de Teste')
        self.assertEqual(new.news_text, 'Notícias')


class CommunityTestCase(TestCase)
    def setUp(self):
        Community.objects.create(
            id = 
            title = 'Comunidade Ecodm'
            category =
            foundation_date =
            begin_visit_time =  
            end_visit_time = 
            longitude = 
            latitude = 
            link = 
            logo =   
        )

    def test_community_criada_com_sucesso(self):
        community = Community.objects.get(nome='Comunidade Ecodm')
        self.assertEqual(community.title, 'Comunidade Ecodm')

    def test_category_da_community(self):
        community = Community.objects.get(nome='Comunidade de Econdm')
        self.assertAlmostEqual(community.category, ['Ponto Turístico', 'Comunidade'])

    def test_begin_visit_time(self):
        community = Community.objects.get(nome='Comunidade Ecodm')
        self.assertIn(community.title, 'Comunidade Ecodm')

    def test_end_visit_time(self):
        community = Community.objects.get(nome='Evento de Teste')
        self.assertGreaterEqual(community.title, 'Comunidade Ecodm')