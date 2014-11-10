__author__ = 'ipetrash'


""""""


class Date:
    """"""

    # Атрибуты
    # xml:lang (опционально) - язык;
    # name="value (опционально)
    #
    # Подчиненные элементы
    # Нет подчиненных элементов, содержит текстовое представление даты.
    #
    # Подчинен
    # Может содержаться в следующих элементах:
    # <title-info> 0..1 (один, опционально);
    # <src-title-info> 0..1 (один, опционально) с версии 2.1;
    # <document-info> 0..1 (один, опционально);
    # <poem> 0..1 (один, опционально).
    #
    # Пример использования
    # <date value="2002-10-19">19.10.2002</date>

    def __init__(self):
        self.day = None
        self.month = None
        self.year = None

    def set_date(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def get_source(self):
        if not self.day or not self.month or not self.year:
            raise NameError('Не до конца указана дата '
                            '(self.day={}, self.month={}, self.year={}).'
                            .format(self.day, self.month, self.year))

        return ('<date value="{2}-{1}-{0}">'
                '{0}.{1}.{2}'
                '</date>').format(self.day, self.month, self.year)