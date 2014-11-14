__author__ = 'ipetrash'


""""""


from pyfb2.title_info import Title_Info
from pyfb2.document_info.document_info import Document_Info
from pyfb2.publish_info.publish_info import Publish_Info
from pyfb2.custom_info import Custom_Info


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
    # <src-title-info> - 0..1 (один, опционально) с версии 2.1;
    # <document-info> - 1 (один, обязателен);
    # <publish-info> - 0..1 (один, опционально);
    # <custom-info> - 0..n (любое число, опционально);
    # <output> - 0..2 (опционально один или два) с версии 2.1.
    # То есть обязательны разделы <title-info> и <document-info>, а остальные
    # добавляются по необходимости.
    #
    # Подчинен
    # Может содержаться в следующих элементах:
    # <FictionBook> - 1 (один, обязателен)

    # TODO: доделать

    def __init__(self):
        self.title_info = Title_Info()  # 1 (один, обязателен);
        # TODO: добавить self.__src_title_info = None  # 0..1 (один, опционально)
        self.document_info = Document_Info()  # 1 (один, обязателен);
        self.__publish_info = None  # 0..1 (один, опционально);
        self.custom_info = Custom_Info()  # 0..n (любое число, опционально);
        # TODO: добавить self.__output = None  # 0..2 (опционально один или два)

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
        source += self.custom_info.get_source()
        source += '</description>'
        return source