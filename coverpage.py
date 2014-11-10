__author__ = 'ipetrash'


""""""


class Coverpage:
    """"""

    # Описание
    # Содержит ссылку на графическое изображение обложки книги.
    #
    # Подчиненные элементы
    # Должен содержать элементы изображений:
    # <image> 1..n (один или несколько, один обязателен).
    #
    # Подчинен
    # Может содержаться в следующих элементах:
    # <title-info> 0..1 (один, опционально);
    # <src-title-info; 0..1 (один, опционально).
    #
    # Пример использования
    # <coverpage><image l:href="#cover.jpg"/></coverpage>

    # TODO: доделать

    def __init__(self):
        self.images = []

    def get_source(self):
        # TODO: проверять список self.images на пустоту
        source = '<coverpage>'
        for im in self.images:
            source += im.get_source()
        source += '</coverpage>'
        return source