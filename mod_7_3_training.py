import string
import os



class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names
    def get_all_words(self):
        """
        Создайте пустой словарь all_words.
Переберите названия файлов и открывайте каждый из них, используя оператор with.
Для каждого файла считывайте единые строки, переводя их в нижний регистр (метод lower()).
Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке. (тире обособлено пробелами, это не дефис в слове).
Разбейте эту строку на элементы списка методом split(). (разбивается по умолчанию по пробелу)
В словарь all_words запишите полученные данные, ключ - название файла, значение - список из слов этого файла.
        """
# правильный вариант
        all_words = {}

        for i in self.file_names:
            with open(i, 'r', encoding="utf-8") as file:
            # режим открытия можно и не указывать
                line = file.read()  # определяем содержимое файла как единую строку!
        # преобразуем в таблицу для удаления пунктуации
                table = str.maketrans("", "", ',.=!?;:-')
                line = line.translate(table)
            # переводим в нижний регистр
                new_line = line.lower()
            # создаём словарь ключ - значение
                all_words[i] = new_line.split()
        return all_words


    def find(self, word):
        """
        word - искомое слово. Возвращает словарь, где ключ - название файла, значение - позиция первого
        такого слова в списке слов этого файла.
        """
        word_list = {}
        word = word.lower()
        for file_names, word in  self.get_all_words().items():
            if word in self.get_all_words().items():
                word_list[file_names] = word.index()
                break

            return word_list

    def count(self, word):
        """
        Возвращает словарь, где ключ - название файла, значение - количество слова word в списке слов этого файла.
        """
        word_count = {}
        count_word = 0
        word = word.lower()
        for file_names, word in  self.get_all_words().items():
            if word in self.get_all_words().items():
                count_word += 1
                word_count[file_names] = count_word
                break

            return word_count









finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
print(finder2.get_all_words().items())
