__author__ = 'ipetrash'


""""""


class Sequence:
    """"""

    # Описание
    # Серия изданий, в которую входит книга, и номер в серии.
    #
    # Атрибуты
    # name (обязательный) - название серии;
    # number (опциональный) - номер книги в серии;
    # xml:lang (опциональный) - язык.
    #
    # Подчиненные элементы
    # Нет дочерних элементов.
    #
    # Подчинен
    # Может содержаться в следующих элементах:
    # <title-info> - 0..n (любое число, опционально);
    # <src-title-info> - 0..n (любое число, опционально);
    # <publish-info> - 0..n (любое число, опционально).
    #
    # Пример использования
    # <sequence name="Грегор Эйзенхорн" number="2"/>

    # TODO: Доделать

    def __init__(self):
        pass

    def get_source(self):
        pass