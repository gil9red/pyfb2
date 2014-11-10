__author__ = 'ipetrash'


from title_info import Title_Info
from document_info import Document_Info


class Description:
    """"""

    # Описание
    # Метаинформация о книге (автор(ы), название, выходные данные, ...) и файле
    # (создатель(и), история, ссылки на источник, ...) Используется в основном
    # библиотечным софтом, но может представлять интерес и рядовому читателю.
    # Рекомендуется серьезно отнесится к заполнению, поскольку неправильно
    # (или неполно) заполненное описание приводит к некорректному позиционированию
    # книги в библиотеке, что затрудняет ее поиск, приводит к появлению "двойников"
    # авторов и просто не позволяет потенциальному читателю составить предварительное
    # мнение о книге.

    # Поля раздела description:
    # <title-info> - 1 (один, обязателен);
    # <document-info> - 1 (один, обязателен);
    # <publish-info> - 0..1 (один, опционально);
    # <custom-info> - 0..n (любое число, опционально);
    # То есть обязательны разделы <title-info> и <document-info>, а остальные
    # добавляются по необходимости.
    #
    # Подчинен
    # Может содержаться в следующих элементах:
    # <FictionBook> - 1 (один, обязателен)

    def __init__(self):
        self.title_info = Title_Info()
        self.document_info = Document_Info()
        self.publish_info = None
        self.custom_info = []

    def get_source(self):
        source = '<description>'
        source += self.title_info.get_source()
        source += self.document_info.get_source()
        if self.publish_info:
            source += self.publish_info.get_source()
        for ci in self.custom_info:
            source += ci.get_source()
        source += '</description>'
        return source