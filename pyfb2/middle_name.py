__author__ = 'ipetrash'


""""""


class Middle_Name:
    """"""

    # Описание
    # Отчество или второе имя автора, переводчика или правообладателя.
    #
    # Атрибуты
    # xml:lang (опциональный) - язык.
    #
    # Подчиненные элементы
    # Нет дочерних элементов, содержит текст - собственно отчество.
    #
    # Подчинен
    # Может содержаться в следующих элементах:
    # <author>;
    # <translator>;
    # <publisher> с версии 2.2.
    #
    # Пример использования
    # <author>
    #   <first-name>Robert</first-name>
    #   <middle-name>Anson</middle-name>
    #   <last-name>Heinlein</last-name>
    # </author>

    # TODO: доделать

    def __init__(self):
        self.lang = None
        self.text = None

    def get_source(self):
        if not self.text:
            raise NameError('Не указано отчество или второе имя автора, переводчика или правообладателя.')

        source = '<middle-name'
        if self.lang:
            source += ' xml:lang="{}"'.format(self.lang)
        source += '>'
        source += self.text
        source += '</middle-name>'
        return source