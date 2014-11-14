__author__ = 'ipetrash'


""""""


class Src_Ocr:
    """"""

    # Описание
    # Автор OCR или оригинального документа, размещенного в online.
    #
    # Атрибуты
    # xml:lang (опциональный)
    #
    # Подчиненные элементы
    # Нет дочерних элементов, содержит текстовое описание источника документа.
    #
    # Подчинен
    # Может содержаться в следующих элементах:
    # <document-info> (опциональный).
    #
    # Пример использования
    # <src-ocr>Файл подготовлен совместно www.olmaglib.com с www.fenzin.org</src-ocr>
    # <src-ocr>Oleg E. Kolesnikov</src-ocr>

    # TODO: доделать

    def __init__(self):
        self.lang = None
        self.text = None

    def get_source(self):
        if not self.text:
            raise NameError('Не указан автор OCR или оригинального документа, '
                            'размещенного в online.')

        source = '<src-ocr'
        if self.lang:
            source += ' xml:lang="{}"'.format(self.lang)
        source += '>'
        source += self.text
        source += '</src-ocr>'
        return source
