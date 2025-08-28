import unittest
from book import Book
from book_manager import BookManager

class TestBookManager(unittest.TestCase):
    def setUp(self):
        self.book_manager = BookManager()

    def test_add_book(self):
        """Test menambahkan buku"""
        book = Book("Pemrograman", "Andi", 2020)
        self.book_manager.add_book(book)
        self.assertEqual(1, self.book_manager.get_book_count())

    def test_remove_existing_book(self):
        """Test menghapus buku yang ada"""
        book = Book("Basis Data", "Erlangga", 2021)
        self.book_manager.add_book(book)
        removed = self.book_manager.remove_book("Basis Data")
        self.assertTrue(removed)
        self.assertEqual(0, self.book_manager.get_book_count())

    #Lengkapi Unit Test dibawah untuk buku yang memang tidak terdapat pada list
    def test_remove_non_existing_book(self):
        """Test menghapus buku yang tidak ada"""
        removed = self.book_manager.remove_book("Basis Data")
        self.assertFalse(removed)
        self.assertEqual(0, self.book_manager.get_book_count())

    #Lengkapi Unit Test dibawah untuk mencari buku berdasarkan penulis
    def test_find_books_by_author(self):
        """Test mencari buku berdasarkan author"""
        buku1 = Book("Pemrograman", "Andi", 2020)
        buku2 = Book("Jaringan", "Budi", 2019)
        buku3 = Book("Basis Data", "Andi", 2021)
        self.book_manager.add_book(buku1)
        self.book_manager.add_book(buku2)
        self.book_manager.add_book(buku3)
        found_books = self.book_manager.find_books_by_author("Andi")
        self.assertEqual(2, len(found_books))

    #Lengkapi Unit Test dibawah untuk seluruh buku yang ada di dalam list
    def test_get_all_books(self):
        """Test mendapatkan semua buku"""
        buku1 = Book("Pemrograman", "Andi", 2020)
        buku2 = Book("Jaringan", "Budi", 2019)
        self.book_manager.add_book(buku1)
        self.book_manager.add_book(buku2)
        all_books = self.book_manager.get_all_books()
        self.assertEqual(2, len(all_books))

if __name__ == '__main__':
    unittest.main()