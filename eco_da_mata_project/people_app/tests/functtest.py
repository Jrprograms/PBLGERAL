from django.test import TestCase, Client
from models import People, Subcategorie

class FunctionalTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.subcategory = Subcategorie.objects.create(name='Exemplo', category='PEOPLE')
        self.people = People.objects.create(
            name='kaiq',
            email='kaiq@email.com',
            description='kaiq é legal',
            category='PEOPLE',
            fk_subcategory=self.subcategory,
            link='www.github.com/kaiq-br',
            )