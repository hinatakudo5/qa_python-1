import pytest

from main import BooksCollector


# ---------- Тесты для добавления книг ----------

@pytest.mark.parametrize('book_name', ['Книга 1', 'Очень важная книга'])
def test_add_new_book_adds_book_without_genre(book_name):
    collector = BooksCollector()

    collector.add_new_book(book_name)

    books = collector.get_books_genre()
    assert book_name in books
    # у только что добавленной книги жанр не задан
    assert books[book_name] is None


def test_add_new_book_does_not_add_book_with_name_longer_than_40():
    collector = BooksCollector()
    long_name = 'А' * 41  # 41 символ

    collector.add_new_book(long_name)

    books = collector.get_books_genre()
    assert long_name not in books


def test_add_new_book_does_not_add_duplicate_book():
    collector = BooksCollector()
    book_name = 'Гарри Поттер'

    collector.add_new_book(book_name)
    collector.add_new_book(book_name)

    books = collector.get_books_genre()
    # одна и та же книга должна быть только один раз
    assert list(books.keys()).count(book_name) == 1


# ---------- Тесты для установки и получения жанра книги ----------

def test_set_book_genre_sets_genre_for_existing_book():
    collector = BooksCollector()
    book_name = 'Безобидная книга'
    collector.add_new_book(book_name)

    # берём любой допустимый жанр
    any_genre = collector.genre[0]

    collector.set_book_genre(book_name, any_genre)

    assert collector.get
