from django.test import TestCase
from models import People, Subcategorie

class SubcategoryTestCase(TestCase):
    def setUp(self):
        self.subcategory = Subcategorie.objects.create(name='Exemplo', category='PEOPLE')
    
    def nameTest(self):
        subcat = Subcategorie.objects.get(nome='Exemplo')
        self.assertEqual(subcat.name)
    
    def categoryTest(self):
        subcat = Subcategorie.objects.get(category='PEOPLE')
        self.assertEqual(subcat.category)

class PeopleTestCase(TestCase):
    def setUp(self):
        People.objects.create(
            name='kaiq',
            email='kaiq@email.com',
            description='kaiq é legal',
            category='PEOPLE',
            fk_subcategory=self.subcategory,
            link='www.github.com/kaiq-br',
            )
    