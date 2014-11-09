__author__ = 'ipetrash'


class Title:
    """"""

    # Описание
    # Название книги, главы, стихотворения
    #
    # Атрибуты
    # xml:lang (опциональный) - язык.
    #
    # Подчиненные элементы
    # Может содержать произвольный набор (в произвольном количестве) из следующих элементов:
    # <p>;
    # <empty-line>.
    #
    # Подчинен
    # Может содержаться в следующих элементах:
    # <body> (опциональный);
    # <section> (опциональный);
    # <poem> (опциональный);
    # <stanza> (опциональный).

    def __init__(self):
        self.text = None
        self.lang = None

    def get_source(self):
        # TODO: доделать
        # TODO: добавить атрибут lang
        return '<title></title>'