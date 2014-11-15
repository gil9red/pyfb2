from enum import Enum


__author__ = 'ipetrash'


# Жанры FictionBook 2.1:
# http://www.fictionbook.org/index.php/Жанры_FictionBook_2.1
# http://www.fictionbook.org/index.php/Eng:FictionBook_2.1_genres

class Genres(Enum):
    # Фантастика (Научная фантастика и Фэнтези)
    sf_history = "sf_history"  # Альтернативная история
    sf_action = "sf_action"  # Боевая фантастика
    sf_epic = "sf_epic"  # Эпическая фантастика
    sf_heroic = "sf_heroic"  # Героическая фантастика
    sf_detective = "sf_detective"  # Детективная фантастика
    sf_cyberpunk = "sf_cyberpunk"  # Киберпанк
    sf_space = "sf_space"  # Космическая фантастика
    sf_social = "sf_social"  # Социально-психологическая фантастика
    sf_horror = "sf_horror"  # Ужасы и Мистика
    sf_humor = "sf_humor"  # Юмористическая фантастика
    sf_fantasy = "sf_fantasy"  # Фэнтези
    sf = "sf"  # Научная Фантастика

    # Детективы и Триллеры
    det_classic = "det_classic"  # Классический детектив
    det_police = "det_police"  # Полицейский детектив
    det_action = "det_action"  # Боевик
    det_irony = "det_irony"  # Иронический детектив
    det_history = "det_history"  # Исторический детектив
    det_espionage = "det_espionage"  # Шпионский детектив
    det_crime = "det_crime"  # Криминальный детектив
    det_political = "det_political"  # Политический детектив
    det_maniac = "det_maniac"  # Маньяки
    det_hard = "det_hard"  # Крутой детектив
    thriller = "thriller"  # Триллер
    detective = "detective"  # Детектив (не относящийся в прочие категории).

    # Проза prose_classic - Классическая проза
    prose_classic = "prose_classic"  # Классическая проза
    prose_history = "prose_history"  # Историческая проза
    prose_contemporary = "prose_contemporary"  # Современная проза
    prose_counter = "prose_counter"  # Контркультура
    prose_rus_classic = "prose_rus_classic"  # Русская классическая проза
    prose_su_classics = "prose_su_classics"  # Советская классическая проза

    # Любовные романы
    love_contemporary = "love_contemporary"  # Современные любовные романы
    love_history = "love_history"  # Исторические любовные романы
    love_detective = "love_detective"  # Остросюжетные любовные романы
    love_short = "love_short"  # Короткие любовные романы
    love_erotica = "love_erotica"  # Эротика

    # Приключения
    adv_western = "adv_western"  # Вестерн
    adv_history = "adv_history"  # Исторические приключения
    adv_indian = "adv_indian"  # Приключения про индейцев
    adv_maritime = "adv_maritime"  # Морские приключения
    adv_geo = "adv_geo"  # Путешествия и география
    adv_animal = "adv_animal"  # Природа и животные
    adventure = "adventure"  # Прочие приключения (то, что не вошло в другие категории)

    # Детское
    child_tale = "child_tale"  # Сказка
    child_verse = "child_verse"  # Детские стихи
    child_prose = "child_prose"  # Детскиая проза
    child_sf = "child_sf"  # Детская фантастика
    child_det = "child_det"  # Детские остросюжетные
    child_adv = "child_adv"  # Детские приключения
    child_education = "child_education"  # Детская образовательная литература
    children = "children"  # Прочая детская литература (то, что не вошло в другие категории)

    # Поэзия, Драматургия
    poetry = "poetry"  # Поэзия
    dramaturgy = "dramaturgy"  # Драматургия

    # Старинное
    antique_ant = "antique_ant"  # Античная литература
    antique_european = "antique_european"  # Европейская старинная литература
    antique_russian = "antique_russian"  # Древнерусская литература
    antique_east = "antique_east"  # Древневосточная литература
    antique_myths = "antique_myths"  # Мифы. Легенды. Эпос
    antique = "antique"  # Прочая старинная литература (то, что не вошло в другие категории)

    # Наука, Образование
    sci_history = "sci_history"  # История
    sci_psychology = "sci_psychology"  # Психология
    sci_culture = "sci_culture"  # Культурология
    sci_religion = "sci_religion"  # Религиоведение
    sci_philosophy = "sci_philosophy"  # Философия
    sci_politics = "sci_politics"  # Политика
    sci_business = "sci_business"  # Деловая литература
    sci_juris = "sci_juris"  # Юриспруденция
    sci_linguistic = "sci_linguistic"  # Языкознание
    sci_medicine = "sci_medicine"  # Медицина
    sci_phys = "sci_phys"  # Физика
    sci_math = "sci_math"  # Математика
    sci_chem = "sci_chem"  # Химия
    sci_biology = "sci_biology"  # Биология
    sci_tech = "sci_tech"  # Технические науки
    science = "science"  # Прочая научная литература (то, что не вошло в другие категории)

    # Компьютеры и Интернет
    comp_www = "comp_www"  # Интернет
    comp_programming = "comp_programming"  # Программирование
    comp_hard = "comp_hard"  # Компьютерное "железо" (аппаратное обеспечение)
    comp_soft = "comp_soft"  # Программы
    comp_db = "comp_db"  # Базы данных
    comp_osnet = "comp_osnet"  # ОС и Сети
    computers = "computers"  # Прочая околокомпьтерная литература (то, что не вошло в другие категории)

    # Справочная литература
    ref_encyc = "ref_encyc"  # Энциклопедии
    ref_dict = "ref_dict"  # Словари
    ref_ref = "ref_ref"  # Справочники
    ref_guide = "ref_guide"  # Руководства
    reference = "reference"  # Прочая справочная литература (то, что не вошло в другие категории)

    # Документальная литература
    nonf_biography = "nonf_biography"  # Биографии и Мемуары
    nonf_publicism = "nonf_publicism"  # Публицистика
    nonf_criticism = "nonf_criticism"  # Критика
    design = "design"  # Искусство и Дизайн
    nonfiction = "nonfiction"  # Прочая документальная литература (то, что не вошло в другие категории)

    # Религия и духовность
    religion_rel = "religion_rel"  # Религия
    religion_esoterics = "religion_esoterics"  # Эзотерика
    religion_self = "religion_self"  # Самосовершенствование
    religion = "religion"  # Прочая религионая литература (то, что не вошло в другие категории)

    # Юмор
    humor_anecdote = "humor_anecdote"  # Анекдоты
    humor_prose = "humor_prose"  # Юмористическая проза
    humor_verse = "humor_verse"  # Юмористические стихи
    humor = "humor"  # Прочий юмор (то, что не вошло в другие категории)

    # Домоводство (Дом и семья)
    home_cooking = "home_cooking"  # Кулинария
    home_pets = "home_pets"  # Домашние животные
    home_crafts = "home_crafts"  # Хобби и ремесла
    home_entertain = "home_entertain"  # Развлечения
    home_health = "home_health"  # Здоровье
    home_garden = "home_garden"  # Сад и огород
    home_diy = "home_diy"  # Сделай сам
    home_sport = "home_sport"  # Спорт
    home_sex = "home_sex"  # Эротика, Секс
    home = "home"  # Прочиее домоводство (то, что не вошло в другие категории)