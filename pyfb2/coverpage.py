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
    # <coverpage><image xlink:href="#cover.jpg"/></coverpage>

    # TODO: доделать

    def __init__(self):
        self.__list = []

    def append(self, image):
        self.__list.append(image)

    def get_source(self):
        if not self.__list:
            raise NameError('Список изображений пуст.')

        source = '<coverpage>'

        for im in self.__list:
            source += im.get_source()

        source += '</coverpage>'
        return source