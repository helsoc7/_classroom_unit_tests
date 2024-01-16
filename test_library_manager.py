import unittest
from library_manager import Book, Library

class Test(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.library.add_book(Book("1984", "George Orwell"))
        self.library.add_book(Book("Der Fänger im Roggen", "J.D. Salinger"))

    def test_get_info(self):
        book = self.library.find_book("1984")
        self.assertEqual(book.get_info(), "1984 von George Orwell")

    def test_find_book(self):
        self.assertIsNotNone(self.library.find_book("1984"))
        self.assertIsNone(self.library.find_book("Unbekanntes Buch"))

    def test_remove_book(self):
        self.library.remove_book("Der Fänger im Roggen")
        self.assertIsNone(self.library.find_book("Der Fänger im Roggen"))
