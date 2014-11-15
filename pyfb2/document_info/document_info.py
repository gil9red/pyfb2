__author__ = 'ipetrash'

""""""

from pyfb2.author import Author
from pyfb2.date import Date
from pyfb2.program_used import Program_Used
from pyfb2.src_url import Src_Url
from pyfb2.src_ocr import Src_Ocr
from pyfb2.id_tag import Id
from pyfb2.version import Version
from pyfb2.history import History
# TODO: 2.2 import publisher_doc_info


class Document_Info:
    """"""

    # Описание информации о конкретном FB2.x документе (создатель(и), история и т.д.).
    #
    # Подчиненные элементы
    # Содержит в перечисленном порядке элементы:
    # <author> - 1..n (любое число, один обязaтелен);
    # <program-used> - 0..1 (один, опционально);
    # <date> - 1 (один, обязателен);
    # <src-url> - 0..n (любое число, опционально);
    # <src-ocr> - 0..1 (один, опционально);
    # <id> - 1 (один, обязателен);
    # <version> - 1 (один, обязателен);
    # <history> - 0..1 (один, опционально);
    # <publisher> - 0..n (любое число, опционально) с версии 2.2.

    # TODO: доделать

    def __init__(self):
        self.author = Author()  # 1..n (любое число, один обязaтелен);
        self.__program_used = None  # 0..1 (один, опционально);
        self.date = Date()  # 1 (один, обязателен);
        self.src_url = Src_Url()  # 0..n (любое число, опционально);
        self.__src_ocr = None  # 0..1 (один, опционально);
        self.id = Id()  # 1 (один, обязателен);
        self.version = Version()  # 1 (один, обязателен);
        self.__history = None  # 0..1 (один, опционально);
        # TODO: 2.2 self.publisher = publisher_doc_info.Publisher()  # 0..n (любое число, опционально) с версии 2.2.

    def get_program_used(self):
        if not self.__program_used:
            self.__program_used = Program_Used()
        return self.__program_used

    program_used = property(get_program_used)

    def get_src_ocr(self):
        if not self.__src_ocr:
            self.__src_ocr = Src_Ocr()
        return self.__src_ocr

    src_ocr = property(get_src_ocr)

    def get_history(self):
        if not self.__history:
            self.__history = History()
        return self.__history

    history = property(get_history)

    def get_source(self):
        source = '<document-info>'
        source += self.author.get_source()
        if self.__program_used:
            source += self.__program_used.get_source()

        source += self.date.get_source()
        source += self.src_url.get_source()

        if self.__src_ocr:
            source += self.__src_ocr.get_source()

        source += self.id.get_source()
        source += self.version.get_source()

        if self.__history:
            source += self.__history.get_source()

        # TODO: 2.2 source += self.publisher.get_source()
        source += '</document-info>'
        return source