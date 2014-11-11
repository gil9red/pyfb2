__author__ = 'ipetrash'


from book_title import Book_Title
from lang import Lang
from keywords import Keywords
from date import Date
from src_lang import Src_Lang
from coverpage import Coverpage
from annotation import Annotation
from sequence import Sequence
from genre import Genre
from author import Author
from translator import Translator


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
        self.annotation = Annotation()  # <annotation> - 0..1 (один, опционально);
        self.keywords = Keywords()  # <keywords> - 0..1 (один, опционально);
        self.date = Date()  # <date> - 0..1 (один, опционально);
        self.coverpage = Coverpage()  # <coverpage> - 0..1 (один, опционально);
        self.lang = Lang()  # <lang> - 1 (один, обязателен);
        self.src_lang = Src_Lang()  # <src-lang> - 0..1 (один, опционально);
        self.translator = Translator()  # <translator> - 0..n (любое число, опционально);
        self.sequence = Sequence()  # <sequence> - 0..n (любое число, опционально).

    def get_source(self):
        # TODO: доделать
        source = '<title-info>'
        source += self.genre.get_source()
        source += self.author.get_source()
        source += self.book_title.get_source()
        source += self.annotation.get_source()
        source += self.keywords.get_source()
        source += self.date.get_source()
        source += self.coverpage.get_source()
        source += self.lang.get_source()
        source += self.src_lang.get_source()
        source += self.translator.get_source()
        source += self.sequence.get_source()
        source += '</title-info>'
        return source