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
    
    def nameTest(self):
        people = People.objects.get(name='kaiq')
        self.assertEqual(people.name)
    
    def emailTest(self):
        people = People.objects.get(email='kaiq@email.com')
        self.assertEqual(people.email)
    
    def categoryTest(self):
        people = People.objects.get(category='PEOPLE')
        self.assertEqual(people.category)
    
    def subcategoriyTest(self):
        people = People.objects.get(fk_subcategory=self.subcategory)
        self.assertEqual(people.fk_subcategory)
    