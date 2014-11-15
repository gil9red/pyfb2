__author__ = 'ipetrash'

""""""


# URL: http://www.fictionbook.org/index.php/Элемент_home-page


class Home_Page:
    """"""

    # Описание
    # Сайт автора, переводчика или правообладателя книги.
    #
    # Подчиненные элементы
    # Нет дочерних элементов, содержит текст - собственно адрес сайта.
    #
    # Подчинен
    # Может содержаться в следующих элементах:
    # <author> 0..n (любое число, опционально);
    # <translator> 0..n (любое число, опционально);
    # <publisher> 0..n (любое число, опционально), с версии 2.2.

    # TODO: доделать

    def __init__(self):
        self.__list = []

    def append(self, home_page):
        if isinstance(home_page, list):
            for i in home_page:
                self.append(i)
        else:
            self.__list.append(home_page)

    def remove(self, home_page):
        self.home_page.remove(home_page)

    def get_source(self):
        source = ''

        for i in self.__list:
            source += '<home-page>{}</home-page>'.format(i)

        return source