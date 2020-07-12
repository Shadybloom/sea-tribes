#----
# Пастбище, сенокос:

metadict_detail['Трава луговая (центнер)'] = {
        # Исправить
            # Уточни по климату с летними и зимними пастбищами.
            # Летние -- в степях, зимние -- в предгорье.
        # Поедаемость трав крупным рогатым скотом -- 50%, овцами -- 60-80%
        # Типичные степные пастбища за сезон дают 20—30 ц/га зелёной массы.
            # http://башкирская-энциклопедия.рф/2-statya/11003-estestvennye-kormovye-ugodya.html
            # https://www.gumer.info/bibliotek_Buks/History/milov/01_7.php
        '|-Пастбище летнее (гектар)':1 / (25 * 0.5) * 0.4,
        '|-Пастбище зимнее (гектар)':1 / (25 * 0.5) * 0.6,
        }

metadict_detail['Трава луговая для овец (центнер)'] = {
        '|-Пастбище летнее (гектар)':1 / (25 * 0.7) * 0.4,
        '|-Пастбище зимнее (гектар)':1 / (25 * 0.7) * 0.6,
        }

metadict_detail['|-Пастбище зимнее (гектар)'] = {
        # Зимние пастбища в предгорье/горах.
        '|--Пастбище (гектар)':1,
        }

metadict_detail['|-Пастбище летнее (гектар)'] = {
        # Залежные степные земли: 3 года земледелия, 9+ лет отдыха.
        # Используются как летнее пастбище.
        '|--Перелог (гектар)':1,
        }

metadict_detail['|--Пастбище (гектар)'] = {
        '|---Пастбище (квадратный километр)':1 / 100,
        }

metadict_detail['|--Перелог (гектар)'] = {
        '|---Перелог (квадратный километр)':1 / 100,
        }


#----
# Зерновые:

metadict_detail['Выращивание пшеницы (центнер)'] = {
        # В урожайности не учитывается доля посева.
            # Нормы высева -- 160-270 кг/га (то есть урожайность сам-4)
        '|-Поля пшеницы (гектар)':1 / 6,
        }

metadict_detail['Выращивание ячменя (центнер)'] = {
        # https://ru.wikisource.org/wiki/ЭСБЕ/Ячмень,_в_сельском_хозяйстве_и_торговле
        '|-Поля ячменя (гектар)':1 / 8,
        }

metadict_detail['Выращивание просо (центнер)'] = {
        '|-Поля просо (гектар)':1 / 6,
        }

metadict_detail['Выращивание риса посевного (центнер)'] = {
        # Период вегитации 150 дней (100 дней поля затоплены), температура 22-30 градусов.
            # https://ru.wikisource.org/wiki/ЭСБЕ/Рис,_в_сельском_хозяйстве_и_мировой_экономике
        '|-Поля риса посевного (гектар)':1 / 10,
        }

#----
# Зерновые-масличные:

metadict_detail['Выращивание льна масличного (центнер)'] = {
        # С десятины урожай семян сам-3, сам-4, а волокна до 10 пудов (164 кг) (в урожайный год)
        '|-Поля льна (гектар)':1 / 4,
        }

#----
# Бобовые:

metadict_detail['Выращивание чечевицы (центнер)'] = {
        # https://ru.wikisource.org/wiki/ЭСБЕ/Чечевица,_в_сельском_хозяйстве
        '|-Поля чечевицы (гектар)':1 / 6,
        }

metadict_detail['Выращивание гороха посевного (центнер)'] = {
        # Урожайность гороха 5-7 четвертей: 6*0.21*0.7=0.882 тонн/гектар (9 центнеров/гектар)
            # https://ru.wikisource.org/wiki/ЭСБЕ/Горох
            # http://www.activestudy.info/uborka-goroxa-2/
        '|-Поля гороха посевного (гектар)':1 / 6,
        }

metadict_detail['Выращивание нута бараньего (центнер)'] = {
        '|-Поля нута бараньего (гектар)':1 / 6,
        }

#----
# Огородные:

metadict_detail['Выращивание капусты белокочанной (центнер)'] = {
        '|-Поля капусты белокочанной (гектар)':1 / 150,
        }

metadict_detail['Выращивание моркови (центнер)'] = {
        # Средний урожай -- 200 центнеров с гектара/год
            # Три урожая за лето
            # https://ru.wikisource.org/wiki/ЭСБЕ/Морковь
        '|-Поля моркови (гектар)':1 / 150,
        }

metadict_detail['Выращивание лука репчатого (центнер)'] = {
        '|-Поля лука репчатого (гектар)':1 / 100,
        }

metadict_detail['Выращивание лука зелёного (центнер)'] = {
        '|-Поля лука зелёного (гектар)':1 / 150,
        }

metadict_detail['Выращивание чеснока (центнер)'] = {
        '|-Поля чеснока (гектар)':1 / 50,
        }

#----
# Садовые:

metadict_detail['Выращивание винограда (центнер)'] = {
        # Около 1000 литров вина с гектара по Кавказскому краю:
            # https://ru.wikisource.org/wiki/ЭСБЕ/Виноградарство
            # http://vinograd.info/info/vinogradarstvo-po-novomy/gystota-posadki.html
        '|-Виноградники (гектар)':1 / 30,
        }

metadict_detail['Выращивание оливок (центнер)'] = {
        # С одного дерева 1-3 литра масла.
        # Собирают оливки постелив под деревом ткань. Они сами падают.
        '|-Оливковые сады (гектар)':1 / 10,
        }

metadict_detail['Выращивание яблок (центнер)'] = {
        '|-Яблоневые сады (гектар)':1 / 30,
        }

metadict_detail['Выращивание алычи (центнер)'] = {
        # Исправить
            # Это дикорастущая слива.
        '|-Сливовые сады (гектар)':1 / 20,
        }

metadict_detail['Выращивание сливы (центнер)'] = {
        '|-Сливовые сады (гектар)':1 / 30,
        }

metadict_detail['Выращивание граната (центнер)'] = {
        # Урожайность 30-50 килограмм/куст, 500 деревьев/гектар (150 ц/га)
            # http://berrylib.ru/books/item/f00/s00/z0000043/st018.shtml
        '|-Гранатовые сады (гектар)':1 / 30,
        }

metadict_detail['Выращивание груши (центнер)'] = {
        '|-Грушёвые сады (гектар)':1 / 30,
        }

metadict_detail['Выращивание инжира (центнер)'] = {
        # Урожайность 50-140 килограмм/дерево, 156 деревьев/гектар (156 ц/га)
            # http://figtree.com.ua/blog/urozhajnost-inzhira/
        '|-Фиговые сады (гектар)':1 / 30,
        }

#----
# Импорт:

metadict_detail['Выращивание чёрного перца (центнер)'] = {
        '|-Плантации чёрного перца (гектар)':1 / 30,
        }

metadict_detail['Выращивание шафрана (центнер)'] = {
        # 80 000 цветов на гектар
        '|-Плантации шафрана (гектар)':1 / 20,
        }

#----
# Огородничество (трудозатраты):

metadict_detail['|-Поля капусты белокочанной (гектар)'] = {
        # https://ru.wikisource.org/wiki/ЭСБЕ/Огород
        # Гектар картофеля (без механизации) -- 830 нормо-часов (100 рабочих дней)
        # С минимальной механизацией (плуг, картофелесажалка) -- 500 нормо-часов (60 рабочих дней)
        # Один морг (около 0,5 дес.) огорода овощей был равен 9 коне-дням и 199 человеко-дням.
            # Это около 365 нормо-дней/гектар или 3650 нормо-часов/гектар.
            # Какие-то дикие числа, на грани окупаемости по калорийности репы:
            # https://www.gumer.info/bibliotek_Buks/History/milov/01_8.php
        '|--Овощные огороды (гектар)':1,
        }

metadict_detail['|-Поля лука зелёного (гектар)'] = {
        '|--Овощные огороды (гектар)':1,
        }

metadict_detail['|-Поля лука репчатого (гектар)'] = {
        '|--Овощные огороды (гектар)':1,
        }

metadict_detail['|-Поля моркови (гектар)'] = {
        '|--Овощные огороды (гектар)':1,
        }

metadict_detail['|-Поля чеснока (гектар)'] = {
        '|--Овощные огороды (гектар)':1,
        }

#----
# Бобовые (трудозатраты):

metadict_detail['|-Поля гороха посевного (гектар)'] = {
        # Нормы высева -- 220-330 кг/га
            # Четверть гороха -- 2400 кв. саж (140 кг/га).
        '|=Корзина гороха в стручках (килограмм)':250,
        '|--Поля бобовых (гектар)':1,
        '_-Работа в поле бобовых (нормо-часов)':500,
        }

metadict_detail['|-Поля нута бараньего (гектар)'] = {
        # Нормы высева -- 120-200 кг/га
        '|=Корзина нута бараньего в стручках (килограмм)':150,
        '|--Поля бобовых (гектар)':1,
        '_-Работа в поле бобовых (нормо-часов)':500,
        }

metadict_detail['|-Поля чечевицы (гектар)'] = {
        # У Марка Порция Катона "Земледелие" (2 век до нашей эры)
            # http://flibustahezeous3.onion/b/480536/read
            # под чечевицу — 8 (32 дня/гектар);
        # Нормы высева -- 100-200 кг/га
        '|=Корзина чечевицы (килограмм)':150,
        '|--Поля бобовых (гектар)':1,
        '_-Работа в поле бобовых (нормо-часов)':500,
        }

#----
# Технические (зерновые):

metadict_detail['|-Поля пшеницы (гектар)'] = {
        # У Марка Порция Катона "Земледелие" (2 век до нашей эры)
            # http://flibustahezeous3.onion/b/480536/read
            # обработка югера под пшеницу, siligo и полбу
            # (подразумевается вспашка, посев, бороньба, мотыженье, прополка, жатва)
            # требуется 10 1/2 дней (42 дня/гектар);
        # Гектар зерновых (вспашка с плугом и волами) -- 400 нормо-часов (50 рабочих дней)
            # https://www.gumer.info/bibliotek_Buks/History/milov/index.php
            # Монастырское хозяйство (18 век) -- 59.5 нормо-дней/десятина
                # Страда в нечерноземье России -- 130 дней/год
            # Фермерство на севере Франции (18 век) -- 39-42 нормо-дней/гектар
                # Страда на севере Франции -- 230 дней/год
        # Нормы высева -- 160-270 кг/га
            # Четверть пшеницы — 1600 кв. саж. (196-225 кг/гектар)
            # https://www.gumer.info/bibliotek_Buks/History/milov/01_3.php
        '_-Обмолот зерновых (килограмм)':200 / (1 - 0.20),
        '|=Корзина зерна пшеницы (килограмм)':200,
        '|=Сноп пшеницы (килограмм)':200 * (1 / 0.66) / (1 - 0.20),
        '|=Сноп пшеничной соломы (килограмм)':200 * (1 / 0.66 - 1) / (1 - 0.20),
        '+Солома пшеничная (доступно/килограмм)':200 * (1 / 0.66 - 1) / (1 - 0.20),
        '|--Поля зерновых (гектар)':1,
        '_-Работа в поле зерновых (нормо-часов)':400,
        }

metadict_detail['|-Поля ячменя (гектар)'] = {
        # Нормы высева (яровой) -- 160-220 кг/га
            # Четверть ячменя — 2400 кв. саж (115 кг/га).
        '_-Обмолот зерновых (килограмм)':200 / (1 - 0.20),
        '|=Корзина зерна ячменя (килограмм)':200,
        '|=Сноп ячменя (килограмм)':200 * (1 / 0.34) / (1 - 0.20),
        '|=Сноп ячменной соломы (килограмм)':200 * (1 / 0.34 - 1) / (1 - 0.20),
        '+Солома ячменная (доступно/килограмм)':200 * (1 / 0.34 - 1) / (1 - 0.20),
        '|--Поля зерновых (гектар)':1,
        '_-Работа в поле зерновых (нормо-часов)':300,
        }

metadict_detail['|-Поля просо (гектар)'] = {
        # Нормы высева -- 18-22 кг/га
            # https://ru.wikisource.org/wiki/ЭСБЕ/Просо
        '_-Обмолот зерновых (килограмм)':20 / (1 - 0.20),
        '|=Корзина зерна просо (килограмм)':20,
        '|=Сноп просо (килограмм)':20 * (1 / 0.34) / (1 - 0.20),
        '|=Сноп просяной соломы (килограмм)':20 * (1 / 0.34 - 1) / (1 - 0.20),
        '+Солома просяная (доступно/килограмм)':20 * (1 / 0.34 - 1) / (1 - 0.20),
        '|--Поля зерновых (гектар)':1,
        '_-Работа в поле зерновых (нормо-часов)':400,
        }

metadict_detail['|-Поля риса посевного (гектар)'] = {
        # Нормы высева -- 180-230 кг/га
        '_-Обмолот зерновых (килограмм)':200 / (1 - 0.20),
        '|=Корзина зерна риса посевного (килограмм)':200,
        '|=Сноп риса посевного (килограмм)':200 * (1 / 0.66) / (1 - 0.20),
        '|=Сноп рисовой соломы (килограмм)':200 * (1 / 0.66 - 1) / (1 - 0.20),
        '+Солома рисовая (доступно/килограмм)':200 * (1 / 0.66 - 1) / (1 - 0.20),
        '|--Поля зерновых (гектар)':1,
        '_-Работа в поле зерновых (нормо-часов)':1000,
        }

#----
# Технические (трудозатраты):

metadict_detail['|-Поля льна (гектар)'] = {
        # под лен — 11 дней/югер (44 дня/гектар);
        # Нормы высева -- 8 четвериков/десятина (~125 кг/гектар)
        '_-Обмолот масличных культур (килограмм)':125,
        '|=Корзина семян льна (килограмм)':125,
        '|=Сноп льна (килограмм)':125 / 0.33,
        '|--Поля технических культур (гектар)':1,
        '_-Работа в поле зерновых (нормо-часов)':500,
        }

#----
# Сады (трудозатраты):

metadict_detail['|-Виноградники (гектар)'] = {
        # Трудозатраты -- 100 дней на гектар (один рабочий на гектар).
            # http://vinograd.info/info/vinogradarstvo-po-novomy/zatraty-tryda-pri-vysokoshtambovoi-kyltyre.html
        # У Марка Порция Катона "Земледелие" (2 век до нашей эры)
            # http://flibustahezeous3.onion/b/480536/read
            # Виноградник 25 гектаров -- 10-16 рабочих
            # (30000-48000 нормо-часов, 1200-1920 нормо-часов/гектар)
            # При этом гектар виноградника -- 3000 литров вина
        # Виноградник владения Домека, в Хересе, Испания 1856 года:
            # http://az.lib.ru/g/grigorowich_d_w/text_1873_korabl_retvizan.shtml
            # 1500 тонн вина/год, годовой запас в 15 000 бочонков.
            # 200 рабочих (7.5 тонн вина/рабочего), до 1500 сезонных (1 тонна/рабочего)
            # Трудовая стоимость вина (оценочно) от 220 нормо-часов тонну до 630 нормо-часов/тонну.
            # Бутылка хереса - 0.77 литра, бочонок -- 462 литра (11 копеек/литр)
        #'|-Виноград культурный (Vítis vinífera)':10000 / (3.5 * 1.2),
        #'|--Фруктовые сады (гектар)':1,
        '|--Виноградники (гектар)':1,
        '_-Работа на винограднике (нормо-часов)':1000,
        }

metadict_detail['|-Оливковые сады (гектар)'] = {
        # У Марка Порция Катона "Земледелие" (2 век до нашей эры)
            # http://flibustahezeous3.onion/b/480536/read
            # Масличный сад 60 гектаров -- 5-13 рабочих (250-600 нормо-часов/гектар)
        #'|-Олива Эквестрийская (Olea Equestriana)':10000 / (6 * 6),
        #'|--Фруктовые сады (гектар)':1,
        '|--Оливковые сады (гектар)':1,
        '_-Работа на оливковых садах (нормо-часов)':500,
        }

metadict_detail['|-Яблоневые сады (гектар)'] = {
        # Астраханские сады 1785 год:
            # https://www.gumer.info/bibliotek_Buks/History/milov/01_8.php
            # 2 постоянных работника на гектар, 2 сезонных на два месяца (600 нормо-часов?)
        # Современное садоводство на Украине (520 га):
            # http://infoindustria.com.ua/etalon-yablonevogo-sada/
            # 300-500 работников, в сезон 1000 (1-2 работника/гектар)
        # ТИПОВЫЕ НОРМЫ ВЫРАБОТКИ НА МЕХАНИЗИРОВАННЫЕ И РУЧНЫЕ РАБОТЫ В САДОВОДСТВЕ, ВИНОГРАДАРСТВЕ И ПИТОМНИКОВОДСТВЕ
        # http://www.libussr.ru/doc_ussr/usr_14391.htm
        # Технологическая карта, выращивание яблок:
        # http://mehanik-ua.ru/tekhnologicheskie-karty/1470-tekhnologicheskaya-karta-vyrashchivaniya-yablok.html
        # Уход за садом (14 дней/гектар) и уборка яблок (6 дней на гектар). Всего 20 дней/гектар
        #'|-Яблоня карликовая (Malus pumila)':10000 / (3.2 * 3.2),
        '|--Фруктовые сады (гектар)':1,
        '_-Работа во фруктовых садах (нормо-часов)':2000,
        }

metadict_detail['|-Гранатовые сады (гектар)'] = {
        #'|-Гранат (Punica)':10000 / (4.5 * 4.5),
        '|--Фруктовые сады (гектар)':1,
        '_-Работа во фруктовых садах (нормо-часов)':2000,
        }

metadict_detail['|-Грушёвые сады (гектар)'] = {
        #'|-Груша обыкновенная (Pýrus commúnis)':10000 / (6 * 4),
        '|--Фруктовые сады (гектар)':1,
        '_-Работа во фруктовых садах (нормо-часов)':2000,
        }

metadict_detail['|-Сливовые сады (гектар)'] = {
        #'|-Слива домашняя (Prúnus doméstica)':10000 / (4 * 4),
        '|--Фруктовые сады (гектар)':1,
        '_-Работа во фруктовых садах (нормо-часов)':2000,
        }

metadict_detail['|-Фиговые сады (гектар)'] = {
        #'|-Фиговое дерево (Fícus cárica)':10000 / (8 * 8),
        '|--Фруктовые сады (гектар)':1,
        '_-Работа во фруктовых садах (нормо-часов)':2000,
        }

#----
# Плантации (трудозатраты):

metadict_detail['|-Плантации чёрного перца (гектар)'] = {
        # Исправить
            # Допилить. Или забить, иморт же.
        }

metadict_detail['|-Плантации шафрана (гектар)'] = {
        }