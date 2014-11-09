__author__ = 'ipetrash'


from image import Image
from title import Title
from section import Section


class Body:
    """"""

    # Атрибуты
    # name - (опционально) - название <body>, устанавливается в "notes" для тела, содержащего сноски.
    # xml:lang - (опционально) - задание языка для <body>
    #
    # Подчиненные элементы
    # Содержит в перечисленном порядке следующие элементаы:
    # <image> - 0..1 (один, опционально) - задается изображение для отображения в начале книги (или конкретного <body>);
    # <title> - 0..1 (один, опционально) - задается заглавие для отображения в начале книги (или конкретного <body>);
    # <epigraph> - 0..n (любое число, опционально) - задаются эпиграфы к книге;
    # <section> - 1..n (любое число, один обязaтелен) - задаются части (главы, прочие структурные единицы) книги;
    #
    # Подчинен
    # Может содержаться в следующих элементах:
    # <FictionBook> (любое число, один обязaтелен)
    #
    # Описание
    # Здесь собственно и находится текст книги.
    # Хотя формально количество и порядок экземпляров <body> не ограничены, но для
    # совместимости с существующим софтом рекомендуется:
    # Помещать весь основной текст документа в первом <body> (сразу после <description>).
    # При наличии в тексте сносок (<a type="note">) сам текст сносок должен размещаться во
    # втором <body> с атрибутом name="notes".
    # При наличии кроме сносок также комментариев и т.п., что в оригинале размещено в конце
    # книги - создается третье <body> с атрибутом name="comments" или без атрибута name.
    # При отсутствии сносок второе и третье <body> должно отсутствовать, а весь текст размещаться
    # в первом.
    #
    # Пример использования
    # <body name="notes">
    #  <title><p>Примечания</p></title>
    #  <section id="note1">
    #   <title>
    #    <p>1</p>
    #   </title>
    #   <p>Известный английский архитектор XVIII века, испытавший в
    #   своем творчестве сильное влияние античной архитектуры. (Здесь и
    #   далее прим. ред.)</p>
    #  </section>
    #  <section id="note2">
    #   <title>
    #    <p>2</p>
    #   </title>
    #   <p>Американский просветитель, живший в XVIII веке</p>
    #  </section>
    # </body>

    def __init__(self):
        self.name = None
        self.lang = None
        self.image = Image()
        self.title = Title()
        self.epigraph = []
        self.section = [Section()]

    def get_source(self):
        name = ' name="{}"'.format(self.name) if self.name else ''
        lang = ' xml:lang="{}"'.format(self.lang) if self.lang else ''
        source = '<body{}{}>'.format(name, lang)

        if self.image:
            source += self.image.get_source()

        if self.title:
            source += self.title.get_source()

        for e in self.epigraph:
            source += e.get_source()

        for s in self.section:
            source += s.get_source()

        source += '</body>'
        return source