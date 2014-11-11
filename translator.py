__author__ = 'ipetrash'


""""""


from person import Person
from person import PersonItem


class TranslatorItem(PersonItem):
    """Информация об переводчике книги.
    Полностью идентичен <author>."""

    # Пример использования
    # <translator>
    #   <first-name>Борис</first-name>
    #   <last-name>Сергеев</last-name>
    # </translator>

    def __init__(self):
        super().__init__()

        self.name_tag = "translator"


class Translator(Person):
    """"""

    def __init__(self):
        super().__init__()

    def get_source(self):
        # Список переводчиков необязательный, поэтому обойдемся
        # без выбрасывания исключения и просто выйдем
        if not self.list:
            return ''

        source = ''
        for p in self.list:
            source += p.get_source()

        return source