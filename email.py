__author__ = 'ipetrash'


""""""


class Email:
    """"""

    # Описание
    # Адрес электронной почты автора, переводчика или правообладателя книги.
    #
    # Подчиненные элементы
    # Нет дочерних элементов, содержит текст - собственно адрес электронной почты.
    #
    # Подчинен
    # Может содержаться в следующих элементах:
    # <author> 0..n (любое число, опционально);
    # <translator> 0..n (любое число, опционально);
    # <publisher> 0..n (любое число, опционально), с версии 2.2.

    # TODO: доделать

    def __init__(self):
        self.__list = []

    def append(self, email):
        if isinstance(email, list):
            for i in email:
                self.append(i)
        else:
            self.__list.append(email)

    def remove(self, email):
        self.home_page.remove(email)

    def get_source(self):
        source = ''

        for i in self.__list:
            source += '<email>{}</email>'.format(i)

        return source