from django.test import TestCase
from django.test.client import Client 
from django.urls import reverse
from project_app.models import *


class ProjectIntegrationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        Project.objects.create(
            name= 'Projeto do Eco da Mata',
            description='Descrição de Projetos',
            link = 'https://www.youtube.com/watch?v=5Vk828XqjDI',
            phone_number = '75 99123-4567',  
            email = 'Mengão@thunderbird.com',
        )
    
    def test_create_project_via_post(self):
        url = reverse('index_projects')
        response = self.client.post(url, {
            'name' = 'Projeto do Eco da Mata',
            'description' = 'Descrição de Projetos',
            'link' = 'https://www.youtube.com/watch?v=5Vk828XqjDI',
            'phone_number' = '75 99123-4567',  
            'email' = 'Mengão@thunderbird.com',

        })

