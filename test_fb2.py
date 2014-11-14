# TODO: 2.2 from publisher_doc_info import PublisherIte
from pyfb2.author import AuthorItem
from pyfb2.translator import TranslatorItem
from pyfb2.paragraph import Paragraph
from pyfb2 import fb2


__author__ = 'ipetrash'


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
    a.first_name.text = "Ilya"
    a.middle_name.text = "Andreevich"
    a.last_name.text = "Petrash"
    a.nickname.text = "gil9red"
    a.home_page.append(["https://github.com/gil9red",
                        "http://vk.com/ipetrash"])
    a.email.append("ip1992@inbox.ru")
    a.id = "777"
    title_info.author.append(a)

    t = TranslatorItem()
    t.first_name.text = "Vasya"
    t.last_name.text = "Pupkin"
    title_info.translator.append(t)


    coverpage = title_info.coverpage
    cover_im = book.append_image(file_name='test_fb2_im.png')
    coverpage.append(cover_im)


    document_info = book.description.document_info
    document_info.author.append(a)
    document_info.program_used.lang = "en"
    document_info.program_used.append(["opera", "word", "notepad"])
    document_info.date.set_date(12, 11, 2014)
    document_info.src_url.append(["www.vk.com", "www.wiki.org", "www.bash.im"])
    document_info.src_ocr.lang = "ru"
    document_info.src_ocr.text = "Vasya Pupkin"
    document_info.id.value = "C03EEC10-4053-4913-86D0-F379926F3487"
    document_info.version.value = "1.0"
    document_info.history.append_paragraph().text = "Первая версия."
    document_info.history.append_empty_line()
    document_info.history.append_paragraph().text = "Бла-бла-бла."
    document_info.history.id = "112211"
    document_info.history.lang = "ru"

    # TODO: 2.2
    # p1 = PublisherItem()
    # p1.first_name.text = "Vasya"
    # p1.last_name.text = "Pupkin"
    # document_info.publisher.append(p1)
    #
    # p2 = PublisherItem()
    # p2.first_name.text = "Ivan"
    # p2.last_name.text = "Ivanov"
    # document_info.publisher.append(p2)


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
    body.doc.image = book.append_image(file_name='test_fb2_im_2.png')
    body.doc.title.append_paragraph().text = "Первая глава"
    body.doc.title.append_paragraph(Paragraph(text="Какой-то текст"))
    body.doc.title.append_empty_line()
    body.doc.title.append_paragraph(Paragraph("Еще текст..."))
    bdt_p = Paragraph(id='001122abc', lang='ru')
    bdt_p.text = "Много текста"
    body.doc.title.append_paragraph(bdt_p)
    body.doc.title.append_empty_line()
    body.doc.title.append_paragraph(Paragraph('Текст после пустой строки'))

    body.notes
    body.comments
    body.append("custom")


    with open('pyfb2_test_fbdoc.fb2', mode='w', encoding='utf-8') as f:
        fb2_source = book.get_source()
        f.write(fb2_source)
        print(fb2_source)