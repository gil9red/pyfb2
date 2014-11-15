__author__ = 'ipetrash'

""""""


class Keywords:
    """"""

    # Описание
    # Список ключевых слов к книге. Предназначен для использования
    # поисковыми системами.
    #
    # Подчиненные элементы
    # Нет подчиненных элементов.
    # Содержит текстовую строку ? собственно список ключевых слов.
    #
    # Подчинен
    # <title-info> - 0..1 (один, опционально);
    # <src-title-info> - 0..1 (один, опционально)

    def __init__(self):
        self.words = []

    def add_keywords(self, word):
        self.words.append(word)

    def remove_keywords(self, word):
        self.words.remove(word)

    def get_source(self):
        return '<keywords>{}</keywords>'.format(', '.join(self.words))