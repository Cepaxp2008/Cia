# Ваша программа должна выполнять следующие
# действия:
# 1. Получить текст от пользователя: Программа
# должна запросить у пользователя ввод строки
# текста.
# 2. Подсчитать количество гласных и согласных букв:
# Определите, какие буквы считаются гласными
# (например, "а", "е", "и", "о", "у", "ы", "э", "ю", "я" в
# русском языке, а также их заглавные эквиваленты).
# Все остальные буквы алфавита считаются
# согласными.
# Учитывайте только буквы русского алфавита,
# игнорируйте цифры, знаки препинания и пробелы.
# 3. Найти самое длинное слово:
# Разделите текст на слова.
# Определите слово с наибольшей длиной.
# Если есть несколько слов одинаковой
# максимальной длины, выведите любое из них.
# 4. Подсчитать количество вхождений заданного
# слова:
# Программа должна запросить у пользователя слово
# для поиска.
# Подсчитайте, сколько раз это слово встречается в
# тексте (без учета регистра).
# Примеры ввода/вывода
# Ввод:
# Введите текст: Привет мир! Это тестовая строка для
# анализа.
# Введите слово для поиска: мир
# Ожидаемый вывод:
# Гласных букв: 12
# Согласных букв: 16
# Самое длинное слово: тестовая
# Слово 'мир' встречается: 1 раз

s = input("Введите строку: ")
t = input("Введите слово для поиска: ")
a = s . upper()
a = a . replace(" " , "")
vowels = "АОУЭЫИЯЕЁЮ"
v = c = 0
for char in a:
    if char in vowels:
        v += 1
    else:
        c += 1
print("Гласных:", v)
print("Согласных:", c)
b = s . split(" ")
c = []
d = 0
for i in b :
    c.append(len(i))
d = c. index(max(c))
print("Самое длинное слово" , b[d])

e = s.upper()
i = t.upper()
f = e.split(" ")
g = 0
for h in f :
    if h == i :
        g += 1
print("Слово" , t , "встречается:" , g , "раз")