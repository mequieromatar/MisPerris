from django.test import TestCase
from GestionPerris.models import *
# Create your tests here

class perroTestCase(TestCase):

    def setUp(self):
        perro.objects.create(foto="perro-collie-corriendo.jpg",nombre_perro="Guau", raza_predominante="Shiba inu",descripcion="descripcion",estado="A")

    def test_perritos_nombre():
        perri = perro.objects.get(nombre_perro="Guau")
        self.assertEqual(perri.perro.descripcion="descripcion")
