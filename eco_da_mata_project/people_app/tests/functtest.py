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
    
    def test_subcategory_creation(self):
        self.assertEqual(self.subcategory.name, 'Exemplo')
        self.assertEqual(self.subcategory.category, 'PEOPLE')

    def test_people_creation(self):
        self.assertEqual(self.people.name, 'kaiq')
        self.assertEqual(self.people.email, 'kaiq@email.com')
        self.assertEqual(self.people.description, 'kaiq é legal')
        self.assertEqual(self.people.category, 'PEOPLE')
        self.assertEqual(self.people.fk_subcategory, self.subcategory)
        self.assertEqual(self.people.link, 'www.github.com/kaiq-br')

    def test_people_list_view(self):
        response = self.client.get('/people/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'kaiq')

    def test_people_detail_view(self):
        response = self.client.get(f'/people/{self.people.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'kaiq')
        self.assertContains(response, 'kaiq@email.com')
        self.assertContains(response, 'kaiq é legal')
        self.assertContains(response, 'www.github.com/kaiq-br')

    def test_people_creation_view(self):
        response = self.client.post('/people/create/', {
            'name': 'novo_nome',
            'email': 'novo_email@email.com',
            'description': 'nova descrição',
            'category': 'PEOPLE',
            'fk_subcategory': self.subcategory.id,
            'link': 'www.novo-link.com',
        })
        self.assertEqual(response.status_code, 302)
        new_people = People.objects.get(name='novo_nome')
        self.assertEqual(new_people.email, 'novo_email@email.com')
        self.assertEqual(new_people.description, 'nova descrição')
        self.assertEqual(new_people.link, 'www.novo-link.com')

    def test_people_update_view(self):
        response = self.client.post(f'/people/{self.people.id}/update/', {
            'name': 'kaiq_atualizado',
            'email': 'kaiq_atualizado@email.com',
            'description': 'descrição atualizada',
            'category': 'PEOPLE',
            'fk_subcategory': self.subcategory.id,
            'link': 'www.atualizado-link.com',
        })
        self.assertEqual(response.status_code, 302)
        updated_people = People.objects.get(id=self.people.id)
        self.assertEqual(updated_people.name, 'kaiq_atualizado')
        self.assertEqual(updated_people.email, 'kaiq_atualizado@email.com')
        self.assertEqual(updated_people.description, 'descrição atualizada')
        self.assertEqual(updated_people.link, 'www.atualizado-link.com')

    def test_people_delete_view(self):
        response = self.client.post(f'/people/{self.people.id}/delete/')
        self.assertEqual(response.status_code, 302)
        with self.assertRaises(People.DoesNotExist):
            People.objects.get(id=self.people.id)