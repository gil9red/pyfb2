from pyfb2.person import Person
from pyfb2.person import PersonItem


__author__ = 'ipetrash'

""""""


class TranslatorItem(PersonItem):
    """Информация об переводчике книги.
    Полностью идентичен <author>."""

    # Пример использования
    # <translator>
    # <first-name>Борис</first-name>
    # <last-name>Сергеев</last-name>
    # </translator>

    # TODO: доделать

    def __init__(self):
        super().__init__()

        self.name_tag = "translator"


class Translator(Person):
    """"""

    # TODO: доделать

    def __init__(self):
        super().__init__()

    def append(self, translator=None):
        if translator:
            self._list.append(translator)
        else:
            translator = TranslatorItem()
            self._list.append(translator)
            return translator

    def get_source(self):
        # Список переводчиков необязательный, поэтому обойдемся
        # без выбрасывания исключения и просто выйдем, если список пуст
        if not self._list:
            return ''

        source = ''
        for p in self._list:
            source += p.get_source()

        return source