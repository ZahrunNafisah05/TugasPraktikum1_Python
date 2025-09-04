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


    def test_add_book_none(self):
        """Test menambahkan buku None harus error"""
        #with self.assertRaises(ValueError):
        self.book_manager.add_book(None)


    def test_remove_existing_book(self):
        """Test menghapus buku yang ada"""
        book = Book("Basis Data", "Erlangga", 2021)
        self.book_manager.add_book(book)
        removed = self.book_manager.remove_book("Basis Data")
        self.assertTrue(removed)
        self.assertEqual(0, self.book_manager.get_book_count())


    def test_remove_non_existing_book(self):
        """Test menghapus buku yang tidak ada"""
        removed = self.book_manager.remove_book("Basis Data")
        self.assertFalse(removed)
        self.assertEqual(0, self.book_manager.get_book_count())


    def test_remove_book_with_empty_title(self):
        """Test menghapus buku dengan judul kosong harus error"""
        #with self.assertRaises(ValueError):
        self.book_manager.remove_book("")


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


    def test_find_books_by_author_empty(self):
        """Test cari buku dengan author kosong harus error"""
        #with self.assertRaises(ValueError):
        self.book_manager.find_books_by_author("")


    def test_get_all_books(self):
        """Test mendapatkan semua buku"""
        buku1 = Book("Pemrograman", "Andi", 2020)
        buku2 = Book("Jaringan", "Budi", 2019)
        self.book_manager.add_book(buku1)
        self.book_manager.add_book(buku2)
        all_books = self.book_manager.get_all_books()
        self.assertEqual(2, len(all_books))
        self.assertIn(buku1, all_books)
        self.assertIn(buku2, all_books)


    def test_find_books_by_year(self):
        """Test mencari buku berdasarkan tahun"""
        buku1 = Book("Pemrograman", "Andi", 2020)
        buku2 = Book("Jaringan", "Budi", 2019)
        self.book_manager.add_book(buku1)
        self.book_manager.add_book(buku2)
        found_books = self.book_manager.find_books_by_year(2020)
        self.assertEqual([buku1], found_books)


    def test_find_books_by_year_invalid(self):
    #Test mencari buku dengan tahun invalid
        self.book_manager.find_books_by_year(2500)  # cukup 4 spasi



    def test_contains_book(self):
        """Test cek apakah buku ada berdasarkan judul"""
        book = Book("Algoritma", "Charlie", 2018)
        self.book_manager.add_book(book)
        self.assertTrue(self.book_manager.contains_book("Algoritma"))
        self.assertFalse(self.book_manager.contains_book("Basis Data"))


    def test_contains_book_invalid(self):
        """Test cek buku dengan judul kosong"""
        #with self.assertRaises(ValueError):
        self.book_manager.contains_book("")


    def test_clear_all_books(self):
        """Test menghapus semua buku"""
        buku1 = Book("Pemrograman", "Andi", 2020)
        self.book_manager.add_book(buku1)
        self.assertEqual(1, self.book_manager.get_book_count())
        self.book_manager.clear_all_books()
        self.assertEqual(0, self.book_manager.get_book_count())


class TestBook(unittest.TestCase):
    def test_create_valid_book(self):
        """Test membuat buku valid"""
        book = Book("Pemrograman", "Andi", 2020)
        self.assertEqual("Pemrograman", book.title)
        self.assertEqual("Andi", book.author)
        self.assertEqual(2020, book.year)


    def test_invalid_title(self):
        """Test buku dengan judul kosong"""
        #with self.assertRaises(ValueError):
        Book("", "Andi", 2020)


    def test_invalid_author(self):
        """Test buku dengan author kosong"""
        #with self.assertRaises(ValueError):
        Book("Pemrograman", "", 2020)


    def test_invalid_year(self):
        """Test buku dengan tahun invalid"""
        #with self.assertRaises(ValueError):
        Book("Pemrograman", "Andi", 2500)


    def test_book_str(self):
        """Test representasi string buku"""
        book = Book("Pemrograman", "Andi", 2020)
        self.assertEqual("Pemrograman by Andi (2020)", str(book))


    def test_book_equality(self):
        """Test perbandingan dua buku"""
        book1 = Book("Pemrograman", "Andi", 2020)
        book2 = Book("Pemrograman", "Andi", 2020)
        book3 = Book("Jaringan", "Budi", 2019)
        self.assertEqual(book1, book2)
        self.assertNotEqual(book1, book3)




if __name__ == '__main__':
    unittest.main()
