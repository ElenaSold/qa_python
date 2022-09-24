from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    #добавление 2х одинаковых книг
    def test_add_new_book_add_two_identical_books(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_new_book('Дюна')
        assert len(collector.get_books_rating()) == 1

    #тестирование назначения рейтинга в пределах от 1 до 10
    def test_set_book_rating_set_rating_9(self):
        collector = BooksCollector()
        collector.add_new_book('Под куполом')
        collector.set_book_rating('Под куполом',9)
        assert collector.get_books_rating()['Под куполом'] == 9

    # тестирование назначения рейтинга выше 10
    def test_set_book_rating_set_rating_11(self):
        collector = BooksCollector()
        collector.add_new_book('Никогде')
        collector.set_book_rating('Никогде',11)
        assert collector.get_books_rating()['Никогде'] == 1

    #тестирование отображения рейтинга по имени книги, которая была добавлена в словарь
    def test_get_book_rating_get_book_rating_by_existing_name(self):
        collector = BooksCollector()
        collector.add_new_book('Искупление')
        assert collector.get_books_rating()['Искупление'] == 1

    #тестирование отображения книг по рейтингу, рейтинг в пределах от 1 до 10
    def test_get_books_with_specific_rating_get_books_with_rating_8(self):
        collector = BooksCollector()
        collector.add_new_book('Гроздья гнева')
        collector.set_book_rating('Гроздья гнева',8)
        assert collector.get_books_with_specific_rating(8)[0] == 'Гроздья гнева'

    #тестирование отображения добавленной книги в books_rating
    def test_get_books_rating_get_books_rating_contains_added_books(self):
        collector = BooksCollector()
        collector.add_new_book('Вокзал потерянных снов')
        assert collector.get_books_rating() == {'Вокзал потерянных снов': 1}

    #тестирование добавления новой книги в избранное
    def test_add_book_in_favorites_add_new_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Ночь в одиноком октябре')
        collector.add_book_in_favorites('Ночь в одиноком октябре')
        assert 'Ночь в одиноком октябре' in collector.get_list_of_favorites_books()

    #тестирование удаления книги из избранного, если она там есть
    def test_delete_book_from_favorites_delete_added_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Скотный двор')
        collector.add_book_in_favorites('Скотный двор')
        collector.delete_book_from_favorites('Скотный двор')
        assert 'Скотный двор' not in collector.get_list_of_favorites_books()

    #тестирование получения избранных книг
    def test_get_list_of_favorites_books_get_list_of_favorites_books_true(self):
        collector = BooksCollector()
        collector.add_new_book('Мы')
        collector.add_book_in_favorites('Мы')
        assert collector.get_list_of_favorites_books()[0] == 'Мы'






