__author__ = 'ipetrash'


""""""


class Custom_Info_Item:
    """"""

    # Описание
    # Некая информация о документе, не предусмотренная в остальной части <description>.
    # Здесь может быть или просто какая-то информация от автора или какая-то информация,
    # могущая быть полезна какому-то FB2 софту.
    #
    # Атрибуты
    # info-type (обязателен) ? некоторое обозначение для данной порции <custom-info>;.
    #
    # Подчиненные элементы
    # Нет подчиненных элементов.
    # Содержит текст, который трактуется программой согласно типу (атрибут info-type) и
    # реализации.
    #
    # Подчинен
    # Может содержаться в следующих элементах:
    # <description> 0..n (любое число, опционально)
    #
    # Пример использования
    # <custom-info info-type="general">
    # Здесь можно расположить дополнительную информацию, не
    # укладывающуюся в заданную схему. Это может быть как описательная
    # информация, так и коммерческая информация, связанная с книгой -
    # например, информация о том, где можно купить бумажное издание
    # </custom-info>

    # TODO: доделать

    def __init__(self):
        self.info_type = None
        self.text = None

    def get_source(self):
        if not self.info_type:
            raise NameError('Не указан атрибут info-type.')

        source = '<custom-info info-type="{}">{}</custom-info>'
        return source.format(self.info_type, self.text)


class Custom_Info:
    """"""

    # TODO: доделать

    def __init__(self):
        self.__list = []

    def append(self, info_type, text):
        # TODO: желательно проверять наличие элемента с таким info_type

        item = Custom_Info_Item()
        item.info_type = info_type
        item.text = text
        self.__list.append(item)

    def get_source(self):
        source = ''

        for s in self.__list:
            source += s.get_source()

        return source