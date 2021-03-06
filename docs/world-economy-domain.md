# Владения

![Глинобитные дома](/images/domain-houses.png)

## Капитал владения

Типичное владение, это селение на 200 домов и 1200 жителей (ремесленников и торговцев), окружённое 30 земледельческими деревнями (10-30 домов, 60-180 жителей) и 50 семейными хозяйствами (2-6 домов, 12-36 жителей). Всё это располагается в регионе размером 6x6 миль (120 квадратных километров), который от края до края можно пройти за пару-тройку часов.  

Владения обозначены на карте как поля.  

Социум       | Население  | Оборот (эфс/год)   | Налоги (эфс/год)
------------ | ---------- | ------------------ | ---------------
Семья        | 6          | 0.3 - 2            | 0.1 - 0.2
Род          | 36         | 2   - 10           | 0.6 - 1
Клан         | 250        | 10  - 60           | 3   - 6
Племя        | 1500       | 60  - 360          | 20 - 36
Народность   | 6000       | 360 - 1200         | 120 - 120

Семьи, роды и кланы объединены родственными связями, у них общие предки, нередко ещё живые. Кланы и племена объединены тем, что женятся между собой, а народности общими обычаями, жизнью на расстоянии дневного перехода и, чаще всего, одним правителем. Например, вами. Каждый народ может выставить до 500 ополчения и сотню профессиональных солдат. На плату последним и уходит большая часть налогов.  

Налоги в диапазоне от 10 до 33% годового оборота. Последние мало чем отличаются от грабежа, так что народ быстро беднеет, а капитал его тает на глазах. Выгоднее иметь богатый народ со скромными налогами, чем бедняков с высокими. Впрочем, разница не столь велика.  

### Земли (3400 эфесов)

Ниже расчёты для племени в 6000 человек, занимающего 6x6 миль территории (120 км²).

Вывод [army-structure-analyser.py](/scripts/):  

```
Выбрано: Владение Лемнос (Ианта «Дочь бури») 1
----Владения...................... | 1
---Городища....................... | 1
---Селения........................ | 30
---Хутора......................... | 50
--Общины.......................... | 223
--Семьи........................... | 892
--Население....................... | 5,416
-Крупный рогатый скот (голов)..... | 834
-Мелкий рогатый скот (голов)...... | 6,278
|---Пастбища (квадратный километр) | 118
|---Перелог (квадратный километр). | 79 
|--Виноградники (гектар).......... | 458 [550 эфс]
|--Овощные огороды (гектар)....... | 56 [67 эфс]
|--Оливковые сады (гектар)........ | 383 [460 эфс]
|--Поля бобовых (гектар).......... | 239 [287 эфс]
|--Поля зерновых (гектар)......... | 1,624 [1950 эфс]
|--Фруктовые сады (гектар)........ | 61 [73 эфс]
```

Это вывод из иерархической базы данных, где площадь полей вычисляется из рациона жителей, распределённого по сезонам и дням года. Точно так же из рациона выводится поголовье скота и ожидаемая площадь пастбищ, которая всегда завышена, потому что скот кормят и виноградными жмыхами, и давлеными оливами, и даже водорослями — всем, что удаётся найти. Пастбищ не хватает всегда.  

### Жилища (1240 эфесов)

№  | Дом семьи       | число | эфс/дом  | эфесов
-- | --------------- | ----- | -------- | ------
1  | Вождей          | 10    | 8        | 80
2  | Торговцев       | 40    | 4        | 160
3  | Ремесленников   | 150   | 2        | 300
4  | Крестьян        | 700   | 1        | 700

Вожди, это вы с офицерами и свитой. Торговцы приносят добрую половину (а может и большую часть) ваших доходов. Ремесленники мастерят снаряжение и строят корабли. Что до крестьян, они платят вам честную десятину: в основном не деньгами, а зерном.  

### Транспорт (660 эфесов)

№  | Транспорт          | Число | Свойства                                      | эфс/шт. | эфесов
-- | ------------------ | ----- | --------------------------------------------- |-------- |----------
1  | Триера (трирёма)   | 1     | 7 миль/час, 36 миль/сутки, до 250 экипажа     | 60      | 60
2  | Торговый корабль   | 20    | 4 мили/час, 18 миль/сутки, до 250 пассажиров  | 30      | 600

Типичные торговые суда имеют экипаж в 20-50 человек, а грузоподъёмность в 50-300 тонн (в среднем 75 тонн). Ветер — штука непредсказуемая, поэтому все морские суда имеют хотя бы один ряд вёсел. Огромного экипажа не требуется, потому что соотношение скорость/мощность в гребле, это экспонента. 100 гребцов могут разогнать военную триеру до 7 миль/час, выдавая 13 кВт мощности, а 20 человек экипажа торгового судна легко дадут 4.5 мили/час за 2.6 кВт мощности.  

Обычно торговая наценка 20-50%. Торговец покупает 100 тонн зерна по 30 эфесов, а спустя месяц плавания продаёт за 36. Его выгода с одного похода — 6 эфесов, а за торговый сезон (6 месяцев) — 36 эфесов. Немного, но и немало, хватает и на экипаж, и на «амортизацию» судна, и на достойную жизнь семьи. Если не мучить его неподъёмными налогами, он будет платить вам 0.3 эфеса/месяц (3.6 эфеса/год). Добрую половину доходов с владения дают именно эти скромные трудяги.  

Торговлю шеститысячного морского народа обеспечивают 20 невеликих парусных судов, а их экипажи — 500 человек. Эти люди — ваши ополченцы. Если нужно, вы легко можете перебросить их по морю, чтобы использовать в бою.

- Стоимость триеры (40-70 эфесов, 6000 человеко-дней).  
- Венецианская морская торговля (45 галер, 300 больших судов (125 тонн груза 25 экипажа), 3000 меньших)  

### Ценности (500 эфесов)

№  | Товар                | эфс/тонна   | тонн  | эфесов
-- | -------------------- | ----------- | ----- | --------------
1  | Керамическая посуда  | 0.3         | 240   | 70
2  | Деревянная мебель    | 1           | 80    | 80
3  | Чугунная утварь      | 2.5         | 30    | 80
4  | Железные инструменты | 5.6         | 15    | 80
5  | Шерстяная пряжа      | 8.3         | 9     | 80
6  | Бронзовые поделки    | 28          | 3     | 80

Упомянуты только товары высокого качества. Тонкая шерсть на продажу, мебель из домов торговцев, сделанная умелым гончаром керамическая посуда. Запас шерсти от местных овец есть всегда, а продают её, когда изготовят достаточно хорошей пряжи. Бронзовые поделки, это в основном посуда и украшения в домах богатых жителей, а чугунные и железные — котлы и инструменты.  

Один товар будет значительно преобладать над другими, если поселение специализируется на его продаже.  

- Римская металлургия (железо — 0.7-1.5 кг/человека-год, медь 0.27 кг/человека-год).
- Хороший гончар делает 70-140 горшков/день (0.3 эфеса/1000 малых горшков)
- Пифос на 100 литров = 40 кг. Это основная тара для любых припасов.

### Скот (370 эфесов)

№  | Товар       | тонн/100 шт. | эфс/100 шт. | голов | тонн  | эфесов
-- | ----------- | ------------ | ----------- | ----- | ----- | ------
1  | Лошади      | 30           | 100         | 10    | 3     | 10
2  | Ослы, мулы  | 30           | 30          | 40    | 12    | 12
3  | Волы        | 50           | 30          | 300   | 150   | 90
4  | Коровы      | 30           | 20          | 600   | 180   | 120
5  | Овцы и козы | 3            | 2           | 6000  | 180   | 120
6  | Куры        | 0.12         | 0.1         | 10000 | 12    | 10

Скотина низкорослая, доится плохо. Это не современные коровы молочных пород, а именно те животные, какими они были в античности.  

- 1 корова = 18 кг шкуры и 0.5 кг сухожилий.
- 1 овца = 60 литров молока/год, 1.4 кг шерсти, 1 ягнёнок
- 1 корова = 600 литров молока/год, 1 телёнок
- 1 курица = 30 яиц/год

### Запасы основные (600 эфесов)

В этой таблице список припасов, которые съедают за год. Запасают примерно столько же: в плохой год спасаются этим, в хороший год излишки продают.

№  | Товар             | эфс/тонна   | тонн  | эфесов
-- | ----------------- | ----------- | ----- | --------------
1  | Вино красное      | 0.3 - 1.5   | 500   | 150
2  | Зерно пшеницы     | 0.3 - 0.6   | 500   | 150
3  | Зерно ячменя      | 0.2 - 0.3   | 400   | 80
4  | Бобы (горох, нут) | 0.3 - 0.6   | 120   | 36
5  | Рыба вяленая      | 0.7         | 110   | 80
6  | Масло оливковое   | 1.2         | 40    | 90

Морская рыба, это основной источник белка в рационе. Осетра, севрюгу и белугу бьют в огромном количестве, когда к лету и осени на реках Котте и Нерет начинается нерест. Рыбу вялят и сушат, сохраняя так на долгие месяцы, а запас регулярно пополняют уловом местных рыбаков.

- 1 кг. рыбы вяленой = 4-6 кг. живого веса рыбы
- 1 кг. солонины = 3.6 кг. живого веса коровы

```
Выбрано: Рыбацкий весенний повседневный рацион (человек/день) 1000
-Рыночная цена (фоллисов).. | 1,787

---Калорийность пищи (килокалорий) | 3,100
-Белки животные (грамм)................. | 46
-Жиры животные (грамм).................. | 35
-Углеводы животные (грамм).............. | 21
-Белки растительные (грамм)............. | 84
-Жиры растительные (грамм).............. | 45
-Углеводы растительные (грамм).......... | 453

Выбрано: Рыбацкий весенний повседневный рацион (человек/день) 1
Вино красное разбавленное (грамм)............. | 1,250
Каша перловая с рыбой и овощами (грамм)....... | 500
Каша ячневая (грамм).......................... | 250
Лаваш пшеничный (грамм)....................... | 200
Лепёшки ячменно-пшеничные на сыворотке (грамм) | 200
Рыба морская красная вяленая (грамм).......... | 125
Суп-пюре чечевичный с пряной зеленью (грамм).. | 500
```

### Запасы прочие (90 эфесов)

№  | Товар             | эфс/тонна   | тонн  | эфесов
-- | ----------------- | ----------- | ----- | --------------
1  | Овощи             | 0.04 - 0.08 | 650   | 26
2  | Фрукты сушёные    | 0.35 - 0.7  | 40    | 12
3  | Сыр овечий        | 0.7         | 16    | 11
4  | Солонина          | 0.8 - 1.4   | 16    | 11
5  | Орехи (миндаль)   | 1.2         | 15    | 18
6  | Пряные травы суш. | 2.4         | 5     | 12

Местные фрукты, это инжир и гранат, алыча и слива, груши, яблоки, персики и вездесущий виноград. Летом и осенью деревья плодоносят, а в сезон дождей люди обходятся сухофруктами. Изрядный запас сухофруктов есть всегда. Главные овощи, это лук, капуста и морковь. Их тушат и обжаривают в масле, дополняя ячменную кашу, а кроме того собирают и выращивают множество пряных трав. Солонину и сыры хранят по случаю, а орехи для путешествий.  

- 1 кг. сухофруктов = 6-10 кг. фруктов
- 1 кг. пряных трав сушёных = 10 кг. зелени

## Демография племени

Вывод [demography-calculator.py](/scripts/demography-calculator.py) (распределение Гомпертца-Мейкхама):  

- Ожидаемая численность: 6000
- Численность популяции: 6043
- Суммарный коэффициент рождаемости: 4.2 (3.8 детей в семье)

Смертность:  
- Смертность общая (в год): 103 (2% от численности населения)
- Несчастные случаи (в год): 54 (53% от числа смертей)
- Военные потери армии (в год): 16 (29% от несчастных случаев)

Средний возраст популяции: 18  
- Дети (0-6 лет) -- 1173 (19%)
- Подростки (6-15 лет) -- 1381 (23%)
- Взрослые (15-50 лет) -- 2704 (45%)
- Старики (50+ лет) -- 785 (13%)

Возрастной состав:  
- 0 -- 212 (4%)
- 1-9 -- 1625 (27%)
- 10-19 -- 1325 (22%)
- 20-29 -- 949 (16%)
- 30-39 -- 674 (11%)
- 40-49 -- 473 (8%)
- 50-59 -- 324 (5%)
- 60-69 -- 213 (4%)
- 70-79 -- 131 (2%)
- 80-89 -- 70 (1%)
- 90-99 -- 33 (1%)
- 100-109 -- 13 (0%)
- 110-119 -- 1 (0%)

Военные и Ветераны по видам войск:  
- Всего (100%) -- 615
- Герои (1%) -- 6
- Наёмники (4%) -- 25
- Ополчение (80%) -- 492
- Регуляры (15%) -- 92

Чтобы сформировать такую армию у нас 75% парней в возрасте 15 лет проходят военную подготовку: то есть забираем всех, кроме совсем уж кривых и косых. После неизбежного отсева (по возрасту и здоровью) 50% мужчин остаются в ополчении, собираясь на тренировки хотя бы пару раз в год, а ваш отряд, это 40% от всех военных в возрасте 20-30 лет (Или 10% от популяции той же возрастной группы).  

Резервов у племени практически нет. Все лучшие в вашем отряде, все способные держать оружие в ополчении. И если бестолочей из ополчения ещё можно кое-как натренировать до уровня отряда, то ополчение уже не из кого пополнить. Разве что девушек начнём в армию брать.  

Обратите внимание на "военные потери". Всего лишь 16 человек в год, или 16% от численности отряда — это ожидаемое и приемлемое число. Их смерть племя ещё может компенсировать, но большие потери уже станут невосполнимыми. В конце года у вас будет всего 40 пятнадцатилетних, годных к военной службе.  

Ваши люди до конца верны вам, в этом всё дело. Их некем заменить.  
