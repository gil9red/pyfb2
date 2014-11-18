__author__ = 'ipetrash'


""""""


class SourceText:
    """"""

    # TODO: доделать

    def __init__(self):
        self.text = None

    def get_source(self):
        if not self.text:
            raise NameError('Не указан исходный текст.')

        return self.text