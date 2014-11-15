__author__ = 'ipetrash'


""""""


class StylesheetItem:
    """"""

    # Описание
    # Здесь содержится таблица стилей, предназначенная для использования
    # программами отображения (или преобразования) книги.
    # На каждый тип таблицы (например ?text/css?) задается отдельный
    # экземпляр <stylesheet>
    #
    # Атрибуты
    # type - Тип таблицы стилей, например "text/css".
    #
    # Подчиненные элементы
    # Нет подчиненных элементов.
    # Содержит текст, который трактуется программой согласно типу (аттрибут "type")
    # и реализации.
    #
    # Пример использования
    # Пример 1.
    # <stylesheet type="text/css">
    #     body{
    #         text-align:justify
    #     }
    #     div.stanza{
    #         margin: 0.4em 0em 0.4em 1em;
    #     }
    # </stylesheet>
    #
    # Пример 2.
    # <stylesheet type="text/css">
    #     span.semi-condensed{
    #        'font-stretch : semi-condensed;
    #     }
    # </stylesheet>
    #
    # ...
    #
    # <p>Normal text <style name="semi-condensed">Semi-condensed text</style> Normal text</p>
    #
    # ...
    #

    def __init__(self, type_stylesheet=None, text_stylesheet=None):
        self.type = type_stylesheet
        self.text = text_stylesheet

    def get_source(self):
        if not self.type or not self.text:
            raise NameError('Не описан тип стиля или содержимое стиля.')

        return '<stylesheet type="{}">{}</stylesheet>'.format(self.type, self.text)


class Stylesheet:
    """"""

    # TODO: доделать

    def __init__(self):
        self.__list = []

    def append(self, type_stylesheet, text_stylesheet):
        ssi = StylesheetItem(type_stylesheet, text_stylesheet)
        self.__list.append(ssi)
        return ssi

    def get_source(self):
        source = ''
        for s in self.__list:
            source += s.get_source()

        return source