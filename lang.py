__author__ = 'ipetrash'


class Lang:
    """"""

    # Описание
    # Язык книги (произведения), если содержится в <title-info>; либо язык
    # оригинала (для переводов), если в <src-title-info>.
    #
    # Подчиненные элементы
    # Нет дочерних элементов, содержит текст - двухбуквенный код языка.
    #
    # Подчинен
    # Может содержаться в следующих элементах:
    # <title-info> 1 (один, обязателен);
    # <src-title-info> 1 (один, обязателен) с версии 2.1.
    #
    # Пример использования
    # <lang>ru</lang>

    def __init__(self):
        self.value = None

    # TODO: Доделать

    def get_source(self):
        if not self.value:
            raise NameError('Не указан язык (self.value is None).')

        return '<lang>{}</lang>'.format(self.value)