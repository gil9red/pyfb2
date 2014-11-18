__author__ = 'ipetrash'

""""""

from pyfb2.person import Person
from pyfb2.person import PersonItem


class AuthorItem(PersonItem):
    """Информация об авторе книги, если элемент используется в <title-info>
    или <src-title-info>; или об авторе документа, если в <document-info>."""

    # Пример использования
    # <author>
    # <first-name>Борис</first-name>
    # <last-name>Сергеев</last-name>
    # </author>

    def __init__(self):
        super().__init__()

        self.name_tag = "author"


class Author(Person):
    """"""

    # TODO: доделать

    def __init__(self):
        super().__init__()

        self.exteption_text_when_empty = 'Список автором пуст.'

    def append(self, author=None):
        if author:
            self._list.append(author)
        else:
            author = AuthorItem()
            self._list.append(author)
            return author