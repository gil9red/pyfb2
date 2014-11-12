from author import AuthorItem
from program_used import Program_Used
from translator import TranslatorItem

import fb2

__author__ = 'ipetrash'

# TODO: xml:lang = http://htmlbook.ru/html/value/lang
# http://www.fictionbook.org/index.php/Пример_документа_в_FB2


if __name__ == '__main__':
    book = fb2.FB2()

    book.stylesheet.append("text/css", "span.semi-condensed{'font-stretch' : semi-condensed;}")

    title_info = book.description.title_info
    title_info.book_title.text = "Мое произведение"
    title_info.annotation.text = ("<p>?Смерть или слава?, ?Черная эстафета?. "
                                  "И теперь наконец - ?Наследие исполинов?!</p>")
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

    from image import Image
    im = Image()
    im.href = "cover"
    title_info.coverpage.append(im)


    document_info = book.description.document_info
    document_info.author.append(a)
    document_info.program_used.lang = "en"
    document_info.program_used.append("opera")
    document_info.program_used.append(["word", "notepad"])
    document_info.program_used.append(["IE", "word", "notepad"])
    document_info.date.set_date(12, 11, 2014)
    document_info.src_url.append("www.vk.com")
    document_info.src_url.append("www.vk.com")
    document_info.src_ocr.lang = "ru"
    document_info.src_ocr.text = "Vasya Pupkin"
    document_info.id.value = "C03EEC10-4053-4913-86D0-F379926F3487"
    document_info.version.value = "1.0"
    # self.history = None  # 0..1 (один, опционально);
    # self.publisher = None  # 0..n (любое число, опционально) с версии 2.2.


    book.binary.append(im.href, "image/jpeg", "/9j/4AAQSkZJRgABAgEAY")
    book.binary.append("im_1", "image/png", "DhAAAAAQ")


    print(book.get_source())