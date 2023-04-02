# Kortezhy
# Task 1
shift = int(input("Введите сдвиг: "))
text = input("Введите текст: ")

alphabet = 'abcdefghijklmnopqrstuvwxyz '
encrypted_text = ''
for char in text:
    if char in alphabet:
        index = alphabet.index(char)
        shifted_index = (index + shift) % len(alphabet)
        encrypted_text += alphabet[shifted_index]
    else:
        encrypted_text += char

print("Зашифрованный текст:", encrypted_text)


# Task 2
fruits = ('apple', 'banana', 'orange', 'banana', 'kiwi', 'banana')
fruit = input("Введите название фрукта: ")
count = fruits.count(fruit)
print("Количество вхождений:", count)


# Task 3
fruits = ('banana', 'apple', 'bananamango', 'mango', 'strawberry-banana')
fruit = input("Введите название фрукта: ")
count = 0
for item in fruits:
    if fruit in item:
        count += item.count(fruit)
print("Количество вхождений:", count)


# Task 4
manufacturers = ('Ford', 'Toyota', 'Honda', 'Toyota', 'BMW', 'Toyota')
manufacturer = input("Введите название производителя: ")
replacement = input("Введите слово для замены: ")
new_manufacturers = []
for item in manufacturers:
    if item == manufacturer:
        new_manufacturers.append(replacement)
    else:
        new_manufacturers.append(item)
new_manufacturers = tuple(new_manufacturers)
print("Новый кортеж производителей:", new_manufacturers)


# Mnozhestva
# Task 1
def superset(set1, set2):
    if set1.issuperset(set2):
        print(f"Объект {set1} является чистым супермножеством")
    elif set2.issuperset(set1):
        print(f"Объект {set2} является чистым супермножеством")
    elif set1 == set2:
        print("Множества равны")
    else:
        print("Супермножество не обнаружено")


set1 = {1, 2, 3, 4, 5, 6}
set2 = {1, 2, 3}
superset(set1, set2)  # Супермножество не обнаружено

set3 = {1, 2, 3, 4, 5, 6}
set4 = {1, 2, 3, 4}
superset(set3, set4)  # Объект {1, 2, 3, 4, 5, 6} является чистым супермножеством

set7 = {1, 2, 3}
set8 = {3, 2, 1}
superset(set7, set8)  # Множества равны


# Task 2
dictionary = {}


def add_word():
    eng_word = input("Введите английское слово: ")
    if eng_word in dictionary:
        print("Слово уже есть в словаре")
        return
    fr_word = input("Введите перевод на французский: ")
    dictionary[eng_word] = fr_word
    print("Слово добавлено в словарь")


def remove_word():
    eng_word = input("Введите английское слово, которое нужно удалить: ")
    if eng_word not in dictionary:
        print("Слово не найдено в словаре")
        return
    del dictionary[eng_word]
    print("Слово удалено из словаря")


def search_word():
    eng_word = input("Введите английское слово для поиска: ")
    if eng_word not in dictionary:
        print("Слово не найдено в словаре")
        return
    print(f"{eng_word} - {dictionary[eng_word]}")


def replace_word():
    eng_word = input("Введите английское слово, которое нужно заменить: ")
    if eng_word not in dictionary:
        print("Слово не найдено в словаре")
        return
    fr_word = input("Введите новый перевод на французский: ")
    dictionary[eng_word] = fr_word
    print("Слово заменено в словаре")


def print_dictionary():
    if not dictionary:
        print("Словарь пуст")
    else:
        print("Английское слово - Перевод на французский")
        for eng_word, fr_word in dictionary.items():
            print(f"{eng_word} - {fr_word}")


while True:
    print("\nМеню:")
    print("1. Добавить слово")
    print("2. Удалить слово")
    print("3. Найти слово")
    print("4. Заменить слово")
    print("5. Вывести весь словарь")
    print("6. Выход")

    choice = input("Выберите действие: ")
    if choice == "1":
        add_word()
    elif choice == "2":
        remove_word()
    elif choice == "3":
        search_word()
    elif choice == "4":
        replace_word()
    elif choice == "5":
        print_dictionary()
    elif choice == "6":
        print("Выход из программы")
        break
    else:
        print("Некорректный выбор")


# Task 3
def set_gen(nums):
    my_set = set()
    for num in nums:
        if nums.count(num) > 1:
            my_set.add(str(num) * nums.count(num))
        else:
            my_set.add(num)
    return my_set


numbers = [1, 2, 3, 4, 4, 4, 5, 5, 6, 6, 6, 6]
result_set = set_gen(numbers)
print(result_set)


# Slovari
# Task 1
def biggest_dict(**kwargs):
    my_dict = {'first_one': 'we can do it'}
    for key, value in kwargs.items():
        my_dict[key] = value
    return my_dict


my_dict = {'first_one': 'we can do it'}
biggest_dict(my_dict, second_one='keep going', third_one='never give up')

print(my_dict)


# Task 2
my_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
my_dict[1], my_dict[5] = my_dict[5], my_dict[1]

del my_dict[2]

my_dict['new_key'] = 'new_value'

print(my_dict)


# Task 3
import json


def add_country(capitals_dict, country, capital):
    capitals_dict[country] = capital


def remove_country(capitals_dict, country):
    if country in capitals_dict:
        del capitals_dict[country]


def search_capital(capitals_dict, country):
    if country in capitals_dict:
        return capitals_dict[country]
    else:
        return None


def edit_country(capitals_dict, country, new_capital):
    if country in capitals_dict:
        capitals_dict[country] = new_capital


def save_data(capitals_dict, filename):
    with open(filename, 'w') as f:
        json.dump(capitals_dict, f)


def load_data(filename):
    with open(filename, 'r') as f:
        return json.load(f)


capitals = {'Russia': 'Moscow', 'USA': 'Washington D.C.', 'France': 'Paris'}

add_country(capitals, 'Germany', 'Berlin')

remove_country(capitals, 'France')

print(search_capital(capitals, 'Russia'))

edit_country(capitals, 'USA', 'New York')

save_data(capitals, 'capitals.json')

new_capitals = load_data('capitals.json')

print(new_capitals)
