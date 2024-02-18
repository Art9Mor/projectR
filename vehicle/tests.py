from rest_framework import status
from rest_framework.test import APITestCase

from vehicle.models import Car


class VehicleTestCase(APITestCase):
    def setUp(self):
        pass

    def test_create_car(self):
        """
        Testing of cars creating
        """
        data = {
            'title': 'Test Car',
            'description': 'Test Description',
        }
        response = self.client.post(
            '/cars/',
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            response.json(),
            {'id': 1, 'milage': [], 'title': 'Test Car', 'description': 'Test Description', 'owner': None}
        )
        self.assertTrue(
            Car.objects.exists()
        )

    def test_list_car(self):
        """
        Testing of list of cars visual
        """
        Car.objects.create(
            title='List Test', description='List Test'
        )
        response = self.client.get('/cars/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [{'id': 2, 'milage': [], 'title': 'List Test', 'description': 'List Test', 'owner': None}]}
        )
