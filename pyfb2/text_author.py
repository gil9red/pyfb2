__author__ = 'ipetrash'


""""""


class Text_Author:
    """"""

    # Описание
    # Автор текста цитаты или стихотворения.
    #
    # Атрибуты
    # id (опциональный) - Идентификатор (якорь, метка) для ссылок на данный элемент
    # style (опциональный) - стиль параграфа
    # xml:lang (опциональный) - язык.
    #
    # Подчиненные элементы
    # Содержит текст, а таке с версии 2.1 может содержать произвольный набор
    # (в произвольном количестве) из следующих элементов:
    # <strong>;
    # <emphasis>;
    # <style>;
    # <a>;
    # <strikethrough>;
    # <sub>;
    # <sup>;
    # <code>;
    # <image>;
    #
    # Подчинен
    # Может содержаться в следующих элементах:
    # <epigraph>;
    # <cite>;
    # <poem>.

    # TODO: доделать

    def __init__(self, text=None, id=None, style=None, lang=None):
        self.id = id
        self.style = style
        self.lang = lang

        self.text = text

    def get_source(self):
        if not self.text:
            raise NameError('Не указан автор текста цитаты или стихотворения '
                            '<text-author> пуст (self.text is None).')

        source = '<text-author'
        if self.id:
            source += ' id="{}"'.format(self.id)
        if self.style:
            source += ' style="{}"'.format(self.style)
        if self.lang:
            source += ' xml:lang="{}"'.format(self.lang)
        source += '>'
        source += self.text
        source += '</text-author>'
        return source