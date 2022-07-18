from django.test import TestCase,SimpleTestCase

# Create your tests here.
class Simpletests(SimpleTestCase):
    def testhp(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code,200)
    def testap(self):
        response=self.client.get('/about/')
        self.assertEqual(response.status_code,200)    