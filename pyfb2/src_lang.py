__author__ = 'ipetrash'

""""""


class Src_Lang:
    """"""

    # Описание
    # Язык оригинала (для переводов).
    #
    # Подчиненные элементы
    # Нет дочерних элементов, содержит текст - двухбуквенный код языка.
    #
    # Подчинен
    # Может содержаться в следующих элементах:
    # <title-info> - 0..1 (один, опционально);
    # <src-title-info>- 0..1 (один, опционально).
    #
    # Пример использования
    # <src-lang>en</src-lang>

    def __init__(self):
        self.value = None

    # TODO: Доделать

    def get_source(self):
        if not self.value:
            raise NameError('Не указан язык (self.value is None).')

        return '<src-lang>{}</src-lang>'.format(self.value)