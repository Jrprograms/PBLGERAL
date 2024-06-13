from django.test import TestCase
from models import People, Subcategorie

class IntegratedTestCase(TestCase):
    def setUp(self):
        self.subcategory = Subcategorie.objects.create(name='Exemplo', category='PEOPLE')
        self.people = People.objects.create(
            name='kaiq',
            email='kaiq@email.com',
            description='kaiq é legal',
            category='PEOPLE',
            fk_subcategory=self.subcategory,
            link='www.github.com/kaiq-br',
            )