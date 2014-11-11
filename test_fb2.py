from author import AuthorItem
from translator import TranslatorItem

import fb2

__author__ = 'ipetrash'

# TODO: xml:lang = http://htmlbook.ru/html/value/lang
# http://www.fictionbook.org/index.php/Пример_документа_в_FB2


if __name__ == '__main__':
    book = fb2.FB2()

    book.stylesheet.append("text/css", "span.semi-condensed{'font-stretch : semi-condensed;}")

    title_info = book.description.title_info
    title_info.book_title.text = "Мое произведение"
    title_info.book_title.lang = "ru"
    title_info.lang.value = "ru"
    title_info.src_lang.value = "en"
    title_info.keywords.add_keywords("книга")
    title_info.keywords.add_keywords("foo")
    title_info.keywords.add_keywords("github")
    title_info.date.set_date(16, 11, 2014)
    title_info.sequence.append("Война и мир", 1)
    title_info.sequence.append("Горящий пукан школоты", 5, "ru")
    title_info.genre.append("adv_western")
    title_info.genre.append("detective", match=20)

    a = AuthorItem()
    a.first_name = "Ilya"
    a.middle_name = "Andreevich"
    a.last_name = "Petrash"
    a.nickname = "gil9red"
    a.add_home_page("https://github.com/gil9red")
    a.add_home_page("http://vk.com/ipetrash")
    a.add_email("ip1992@inbox.ru")
    a.id = "777"
    title_info.author.append(a)

    t = TranslatorItem()
    t.first_name = "Vasya"
    t.last_name = "Pupkin"
    title_info.translator.append(t)

    # - title_info.annotation = None  # <annotation> - 0..1 (один, опционально);
    # - title_info.coverpage = None  # <coverpage> - 0..1 (один, опционально);


    book.binary.append("cover", "image/jpeg", "/9j/4AAQSkZJRgABAgEAY")
    book.binary.append("im_1", "image/png", "DhAAAAAQ")


    print(book.get_source())