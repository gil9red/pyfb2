__author__ = 'ipetrash'


from title_info import Title_Info
from document_info import Document_Info
from publish_info import Publish_Info


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
        self.title_info = Title_Info()  # 1 (один, обязателен);
        self.document_info = Document_Info()  # 1 (один, обязателен);
        self.__publish_info = None  # 0..1 (один, опционально);
        self.custom_info = []  # 0..n (любое число, опционально);

    def get_publish_info(self):
        if not self.__publish_info:
            self.__publish_info = Publish_Info()
        return self.__publish_info
    publish_info = property(get_publish_info)

    def get_source(self):
        source = '<description>'
        source += self.title_info.get_source()
        source += self.document_info.get_source()
        if self.__publish_info:
            source += self.__publish_info.get_source()
        for ci in self.custom_info:
            source += ci.get_source()
        source += '</description>'
        return source