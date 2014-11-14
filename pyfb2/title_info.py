__author__ = 'ipetrash'


from pyfb2.book_title import Book_Title
from pyfb2.lang import Lang
from pyfb2.keywords import Keywords
from pyfb2.date import Date
from pyfb2.src_lang import Src_Lang
from pyfb2.coverpage import Coverpage
from pyfb2.annotation import Annotation
from pyfb2.sequence import Sequence
from pyfb2.genre import Genre
from pyfb2.author import Author
from pyfb2.translator import Translator


class Title_Info:
    """"""

    # Описание информации о произведении (с учетом перевода, но без учета издания).
    #
    # Подчинен
    # Может содержаться в следующих элементах:
    # <description> - 1 (один, обязателен)

    def __init__(self):
        self.genre = Genre()  # <genre> - 1..n (любое число, один обязaтелен);
        self.author = Author()  # <author> - 1..n (любое число, один обязaтелен);
        self.book_title = Book_Title()  # <book-title> - 1 (один, обязателен);
        self.__annotation = None  # <annotation> - 0..1 (один, опционально);
        self.__keywords = None  # <keywords> - 0..1 (один, опционально);
        self.__date = None  # <date> - 0..1 (один, опционально);
        self.__coverpage = None  # <coverpage> - 0..1 (один, опционально);
        self.lang = Lang()  # <lang> - 1 (один, обязателен);
        self.__src_lang = None  # <src-lang> - 0..1 (один, опционально);
        self.translator = Translator()  # <translator> - 0..n (любое число, опционально);
        self.sequence = Sequence()  # <sequence> - 0..n (любое число, опционально).

    def get_annotation(self):
        if not self.__annotation:
            self.__annotation = Annotation()
        return self.__annotation
    annotation = property(get_annotation)

    def get_keywords(self):
        if not self.__keywords:
            self.__keywords = Keywords()
        return self.__keywords
    keywords = property(get_keywords)

    def get_date(self):
        if not self.__date:
            self.__date = Date()
        return self.__date
    date = property(get_date)

    def get_coverpage(self):
        if not self.__coverpage:
            self.__coverpage = Coverpage()
        return self.__coverpage
    coverpage = property(get_coverpage)

    def get_src_lang(self):
        if not self.__src_lang:
            self.__src_lang = Src_Lang()
        return self.__src_lang
    src_lang = property(get_src_lang)

    def get_source(self):
        # TODO: доделать
        source = '<title-info>'
        source += self.genre.get_source()
        source += self.author.get_source()
        source += self.book_title.get_source()
        if self.__annotation:
            source += self.__annotation.get_source()
        if self.__keywords:
            source += self.__keywords.get_source()
        if self.__date:
            source += self.__date.get_source()
        if self.__coverpage:
            source += self.__coverpage.get_source()
        source += self.lang.get_source()
        if self.__src_lang:
            source += self.__src_lang.get_source()
        source += self.translator.get_source()
        source += self.sequence.get_source()
        source += '</title-info>'
        return source