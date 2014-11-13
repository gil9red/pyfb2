__author__ = 'ipetrash'


from author import AuthorItem
from publisher_doc_info import PublisherItem
from translator import TranslatorItem

import fb2


# TODO: xml:lang = http://htmlbook.ru/html/value/lang
# http://www.fictionbook.org/index.php/Пример_документа_в_FB2

# TODO: лучше бы в каждый модуль добавить ссылку на сайт создателей,
# на определенный элемент fb2.


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
    document_info.src_url.append(["www.vk.com", "www.wiki.org", "www.bash.im"])
    document_info.src_ocr.lang = "ru"
    document_info.src_ocr.text = "Vasya Pupkin"
    document_info.id.value = "C03EEC10-4053-4913-86D0-F379926F3487"
    document_info.version.value = "1.0"
    document_info.history.text = "<p>Первая версия.</p>"
    document_info.history.id = "112211"
    document_info.history.lang = "ru"

    p1 = PublisherItem()
    p1.first_name = "Vasya"
    p1.last_name = "Pupkin"
    document_info.publisher.append(p1)

    p2 = PublisherItem()
    p2.first_name = "Ivan"
    p2.last_name = "Ivanov"
    document_info.publisher.append(p2)


    publish_info = book.description.publish_info
    publish_info.book_name.lang = "ru"
    publish_info.book_name.text = "!Мое! произведение"
    publish_info.publisher.lang = "ru"
    publish_info.publisher.text = "ПрофОригНаф"
    publish_info.city.lang = "ru"
    publish_info.city.text = "Бабруйск"
    publish_info.year.text = "2002"
    publish_info.isbn.lang = "en"
    publish_info.isbn.text = "5-16-002911-7"
    publish_info.sequence.append("Жизнь - Боль", 1, "ru")


    custom_info = book.description.custom_info
    custom_info.append("used", "all")
    custom_info.append("secret_key", "foobar")


    body = book.body
    body.notes
    body.comments
    body.append("custom")


    binary = book.binary
    binary.append(im.href, "image/jpeg", "/9j/4AAQSkZJRgABAgEAY")
    binary.append("im_1", "image/png", "DhAAAAAQ")


    print(book.get_source())