from django.test import TestCase
from project_app.models import *

class ProjectTestCase(TestCase)
    def setUp(self):
        Project.objects.create(
            name = 'Teste',
            description = 'Exame feito para testar, para avaliar as características ou qualidades de algo ou de alguém',
            link = 'https://www.dicio.com.br/teste/',
            phone_number = '11 98273-6455', 
            email = 'Timenopavement@mailspring.com',       
    )

    def test_project_name(self):
        project = Project.objects.get(nome = 'Teste')
        self.assertNotEqual(project.name, '')
        self.assertIsNotNone(project.name)    

    def test_project_description(self):
        project = Project.objects.get(nome = 'Teste') 
        self.assertEqual(project.description, 'Exame feito para testar, para avaliar as características ou qualidades de algo ou de alguém')

    def test_project_link(self):
        project = Project.objects.get(nome = 'Teste')
        self.assertEqual(project.link, 'https://www.dicio.com.br/teste/')

    def test_project_phone_number(self):
        project = Project.objects.get(nome = 'Teste')
        self.assertIn(project.phone_number, '11 98273-6455')

    def test_project_email(self):
        project = Project.objects.get(nome = 'Teste')
        self.assertAlmostEqual(project.email, 'Timenopavement@mailspring.com')

