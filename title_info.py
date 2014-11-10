__author__ = 'ipetrash'


from book_title import Book_Title
from lang import Lang
from keywords import Keywords
from date import Date
from src_lang import Src_Lang


class Title_Info:
    """"""

    # Описание информации о произведении (с учетом перевода, но без учета издания).
    #
    # Подчинен
    # Может содержаться в следующих элементах:
    # <description> - 1 (один, обязателен)

    def __init__(self):
        self.genre = []  # <genre> - 1..n (любое число, один обязaтелен);
        self.author = []  # <author> - 1..n (любое число, один обязaтелен);
        self.book_title = Book_Title()  # <book-title> - 1 (один, обязателен);
        self.annotation = None  # <annotation> - 0..1 (один, опционально);
        self.keywords = Keywords()  # <keywords> - 0..1 (один, опционально);
        self.date = Date()  # <date> - 0..1 (один, опционально);
        self.coverpage = None  # <coverpage> - 0..1 (один, опционально);
        self.lang = Lang()  # <lang> - 1 (один, обязателен);
        self.src_lang = Src_Lang()  # <src-lang> - 0..1 (один, опционально);
        self.translator = []  # <translator> - 0..n (любое число, опционально);
        self.sequence = []  # <sequence> - 0..n (любое число, опционально).

    def get_source(self):
        # TODO: доделать
        source = '<title-info>'

        for g in self.genre:
            source += g.get_source()

        for a in self.author:
            source += a.get_source()

        source += self.book_title.get_source()

        if self.annotation:
            source += self.annotation.get_source()

        if self.keywords:
            source += self.keywords.get_source()

        if self.date:
            source += self.date.get_source()

        if self.coverpage:
            source += self.coverpage.get_source()

        source += self.lang.get_source()

        if self.src_lang:
            source += self.src_lang.get_source()

        for t in self.translator:
            source += t.get_source()

        for s in self.sequence:
            source += s.get_source()

        source += '</title-info>'
        return source