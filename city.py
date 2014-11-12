__author__ = 'ipetrash'


""""""


class City:
    """"""

    # Описание
    # Город, место издания оригинальной (бумажной) книги.
    #
    # Атрибуты
    # xml:lang (опционально) - язык текста.
    #
    # Подчиненные элементы
    # Нет подчиненных элементов, содержит текстовую строку ? собственно название города.
    #
    # Подчинен
    # Может содержаться в следующих элементах:
    # <publish-info> 0..1 (один, опционально).
    #
    # Пример использования
    # <publish-info>
    #   <book-name>Долгин А.Б. Экономика символического обмена</book-name>
    #   <publisher>Инфра-М</publisher>
    #   <city>Москва</city>
    #   <year>2006</year>
    #   <isbn>5-16-002911-7</isbn>
    # </publish-info>

    # TODO: доделать

    def __init__(self):
        self.lang = None
        self.text = None

    def get_source(self):
        if not self.text:
            raise NameError('Не указан город, место издания оригинальной (бумажной) книги.')

        source = '<city'
        if self.lang:
            source += ' xml:lang="{}"'.format(self.lang)
        source += '>'
        source += self.text
        source += '</city>'
        return source