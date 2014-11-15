__author__ = 'ipetrash'

""""""


class Subtitle:
    """"""

    # Описание
    # Смысловой разделитель, имеющий внутри себя текст
    #
    # Атрибуты
    # id (опциональный) - Идентификатор (якорь, метка) для ссылок на данный элемент
    # style (опциональный) - стиль параграфа
    # xml:lang (опциональный) - язык.
    #
    # Подчиненные элементы
    # Содержит текст, а также произвольный набор (в произвольном количестве) из следующих элементов:
    # <strong>;
    # <emphasis>;
    # <style>;
    # <a>;
    # <strikethrough>;
    # <sub>;
    # <sup>;
    # <code>;
    # <image>.
    #
    # Подчинен
    # Может содержаться в следующих элементах:
    # <section>;
    # <cite>;
    # <stanza>;
    # <title-info>;
    # <src-title-info>;
    # <history>.

    # TODO: доделать

    def __init__(self, text=None, id=None, style=None, lang=None):
        self.id = id  # Идентификатор (якорь, метка) для ссылок на данный элемент
        self.style = style  # Стиль параграфа
        self.lang = lang  # Язык

        self.text = text

    def get_source(self):
        if not self.text:
            self.text = "* * *"
            # raise NameError('Не указан подзаголовок: объект {}.'.format(self))

        source = '<subtitle'
        if self.id:
            source += ' id="{}"'.format(self.id)

        if self.style:
            source += ' style="{}"'.format(self.style)

        if self.lang:
            source += ' xml:lang="{}"'.format(self.lang)

        source += '>'
        source += self.text
        source += '</subtitle>'
        return source