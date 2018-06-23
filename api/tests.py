from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Tarea

# Create your tests here.


class ModelTestCase(TestCase):

    """ This class defines the test for application models """

    def setUp(self):
        """It defines test clients and other variables"""
        self.tarea_title = "Test setup"
        self.user = User.objects.create(username='tosmak')
        self.tarea = Tarea(title=self.tarea_title, owner=self.user)

    def test_model_creates_a_tarea_successfully(self):
        """it checks if tarea model can create a task"""

        initial_count = Tarea.objects.count()
        self.tarea.save()
        new_count = Tarea.objects.count()

        self.assertIsNot(initial_count, new_count)


class TareaViewTestCase(TestCase):

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.user = User.objects.create(username='tosmak', is_superuser=True)
        self.client.force_authenticate(user=self.user)
        self.tarea_data = {'title': 'some task', 'description': 'some task description', 'owner': self.user.id}

    def test_api_successfully_creates_a_tarea(self):
        self.response = self.client.post('/tareas/', self.tarea_data, format="json")
        self.assertEqual(self.response.data.get('title'), self.tarea_data.get('title'))
        self.assertEqual(self.response.status_code, 201)

    def test_api_not_successfully_creates_a_tarea_when_title_already_exist(self):
        self.client.post('/tareas/', self.tarea_data, format="json")
        self.response = self.client.post('/tareas/', self.tarea_data, format="json")
        self.assertEqual(self.response.status_code, 400)

    def test_api_successfully_get_list_of_all_tarea(self):
        self.client.post('/tareas/', self.tarea_data, format="json")
        self.response = self.client.get('/tareas/')
        self.assertEqual(len(self.response.data), 1)
        self.assertEqual(isinstance(self.response.data, list), True)
        self.assertEqual(self.response.status_code, 200)

    def test_api_successfully_get_a_tarea(self):
        api_response = self.client.post('/tareas/', self.tarea_data, format="json")
        tarea_id=api_response.data.get('id')
        self.response = self.client.get(f'/tareas/{tarea_id}/')
        self.assertEqual(isinstance(self.response.data, dict), True)
        self.assertEqual(self.response.data.get('title'), self.tarea_data.get('title'))
        self.assertEqual(self.response.status_code, 200)

    def test_api_successfully_update_a_tarea_title(self):
        api_response = self.client.post('/tareas/', self.tarea_data, format="json")
        tarea_id=api_response.data.get('id')
        new_tarea_title={'title': 'title changed', 'owner': self.user.id}
        self.response = self.client.put(f'/tareas/{tarea_id}/', new_tarea_title )
        self.assertEqual(self.response.data.get('title'), new_tarea_title.get('title'))
        self.assertEqual(self.response.status_code, 200)

    def test_api_successfully_update_a_tarea_description(self):
        api_response = self.client.post('/tareas/', self.tarea_data, format="json")
        tarea_id=api_response.data.get('id')
        new_tarea_description={'title': 'title changed', 'owner': self.user.id}
        self.response = self.client.put(f'/tareas/{tarea_id}/', new_tarea_description )
        self.assertEqual(self.response.data.get('title'), new_tarea_description.get('title'))
        self.assertEqual(self.response.status_code, 200)


