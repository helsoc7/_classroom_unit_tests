import unittest
from animal_collection import Animal, Dog, Cat, AnimalCollection

class Test(unittest.TestCase):
    def setUp(self):
        self.collection = AnimalCollection()
        self.collection.add_animal(Dog("Bello"))
        self.collection.add_animal(Cat("Whiskers"))

    def test_get_animal_sound(self):
        self.assertEqual(self.collection.get_animal_sound("Bello"), "Bellen")
        self.assertEqual(self.collection.get_animal_sound("Whiskers"), "Miauen")
        self.assertIsNone(self.collection.get_animal_sound("Unbekanntes Tier"))
