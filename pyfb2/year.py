__author__ = 'ipetrash'

""""""


class Year:
    """"""

    # Описание
    # Год издания оригинальной (бумажной) книги.
    #
    # Атрибуты
    # Нет атрибутов.
    #
    # Подчиненные элементы
    # Нет подчиненных элементов.
    # Содержит текстовую строку ? собственно год издания книги.
    #
    # Подчинен
    # Может содержаться в следующих элементах:
    # <publish-info> (опционально).
    #
    # Пример использования
    # <publish-info>
    # <book-name>Долгин А.Б. Экономика символического обмена</book-name>
    # <publisher>Инфра-М</publisher>
    #   <city>Москва</city>
    #   <year>2006</year>
    #   <isbn>5-16-002911-7</isbn>
    # </publish-info>

    # TODO: доделать

    def __init__(self):
        self.text = None

    def get_source(self):
        if not self.text:
            raise NameError('Не указан год издания оригинальной (бумажной) книги.')

        return '<year>{}</year>'.format(self.text)