__author__ = 'ipetrash'


""""""


from sequence import Sequence
from book_name import Book_Name
import publisher_pub_info
from city import City
from year import Year


class Publish_Info:
    """"""

    # Описание
    # Информация о бумажном (или другом) издании, на основании которого создан
    # FB2.x документ. Не рекомендуется заполнять данными от произвольного издания
    # если не известен источник, за исключением случая, когда по нему проводилась
    # выверка и документ приведен к виду этого издания. Если же источник неизвестен,
    # то лучше вообще опустить данный элемент.
    #
    # Подчиненные элементы
    # Должен содержать в перечисленном порядке:
    # <book-name> - 0..1 (один, опционально) - название;
    # <publisher> - 0..1 (один, опционально) - издательство;
    # <city> - 0..1 (один, опционально)- место издания;
    # <year> - 0..1 (один, опционально) - год издания;
    # <isbn> - 0..1 (один, опционально) - ISBN издания;
    # <sequence> - 0..n (любое число, опционально) - серия (серии) изданий,
    # в которую входит книга.
    #
    # Подчинен
    # Может включаться в следующие элементы:
    # <description> 0..1 (один, опционально)
    #
    # Пример использования
    # <publish-info>
    #  <book-name>Долгин А.Б. Экономика символического обмена</book-name>
    #  <publisher>Инфра-М</publisher>
    #  <city>Москва</city>
    #  <year>2006</year>
    #  <isbn>5-16-002911-7</isbn>
    # </publish-info>

    # TODO: Доделать

    def __init__(self):
        self.__book_name = None  # 0..1 (один, опционально)
        self.__publisher = None  # 0..1 (один, опционально)
        self.__city = None  # 0..1 (один, опционально)
        self.__year = None  # 0..1 (один, опционально)
        self.__isbn = None  # 0..1 (один, опционально)
        self.sequence = Sequence()  # 0..n (любое число, опционально)

    def get_book_name(self):
        if not self.__book_name:
            self.__book_name = Book_Name()
        return self.__book_name
    book_name = property(get_book_name)

    def get_publisher(self):
        if not self.__publisher:
            self.__publisher = publisher_pub_info.Publisher()
        return self.__publisher
    publisher = property(get_publisher)

    def get_city(self):
        if not self.__city:
            self.__city = City()
        return self.__city
    city = property(get_city)

    def get_year(self):
        if not self.__year:
            self.__year = Year()
        return self.__year
    year = property(get_year)

    # def get_isbn(self):
    #     if not self.__isbn:
    #         self.__isbn = Isbn()
    #     return self.__isbn
    # isbn = property(get_isbn)

    def get_source(self):
        source = '<publish-info>'

        if self.__book_name:
            source += self.__book_name.get_source()

        if self.__publisher:
            source += self.__publisher.get_source()

        if self.__city:
            source += self.__city.get_source()

        if self.__year:
            source += self.__year.get_source()

        if self.__isbn:
            source += self.__isbn.get_source()

        source += self.sequence.get_source()

        source += '</publish-info>'
        return source