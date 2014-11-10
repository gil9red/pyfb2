__author__ = 'ipetrash'


class Book_Title:
    """"""

    # Описание
    # Название произведения. Может как совпадать с названием книги (<book-name>),
    # так и отличаться (например, когда под одной обложкой находится несколько
    # произведений).
    #
    # Атрибуты
    # xml:lang (опционально) ? язык контента.
    #
    # Подчиненные элементы
    # Нет подчиненных элементов, содержит текстовую строку ? собственно название произведения.
    #
    # Подчинен
    # Может содержаться в следующих элементах:
    # <title-info> 1 (один, обязателен);
    # <src-title-info> 1 (один, обязателен)
    #
    # Пример использования
    # <book-title>Рубеж</book-title>

    def __init__(self):
        self.lang = None
        self.text = None

    # TODO: доделать

    def get_source(self):
        if not self.text:
            raise NameError('Нет названия произведения (self.text is None).')

        if self.lang:
            return '<book-title xml:lang="{}">{}</book-title>'.format(self.lang, self.text)
        else:
            return '<book-title>{}</book-title>'.format(self.text)