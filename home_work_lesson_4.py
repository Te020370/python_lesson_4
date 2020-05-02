'''
LIGHT
'''
print('Task_1: Напишите функцию (F): на вход список имен и целое число N; '
      'на выходе список длины N случайных имен из первого списка '
      '(могут повторяться, можно взять значения: количество имен 20, N = 100, '
      'рекомендуется использовать функцию random); ')

list_name = ['Андрей', 'Тимофей', 'Игорь', 'Татьяна', 'Сергей', 'Надежда', 'Александр', 'Анатолий', 'Нина', 'Ксения',
             'Максим', 'Ираида', 'Ольга', 'Екатерина', 'Виталий', 'Мария', 'Юлия', 'Лариса', 'Матвей', 'Максим']
import random
def random_name (names, len_new_list_name):
    return random.choices (names, k=len_new_list_name)

new_list_name = random_name(list_name, len_new_list_name=random.randrange(10,100))
#print(new_list_name)

for i in range(len(new_list_name)):
    print(i, ':', new_list_name[i])


print('Task_2: Напишите функцию вывода самого частого имени из списка на выходе функции F')

def often_name (list_name):
    dict = {}
    for i in list_name:
        dict[i] = list_name.count(i)
    #print(type(dict), dict)

    dict = list(dict.items())
    #print(type(dict), dict)

    dict.sort(key=lambda i: i[1], reverse=True) # x[1]  означает сортировку по Values, т.е. по количеству повторений имени в словаре (имя, количество повторений)
    #print(dict)
    return dict[0][0]

print("Самое частое имя: ", often_name(new_list_name))


print('Task_3: Напишите функцию вывода самой редкой буквы, с которой начинаются имена в списке на выходе функции F')

def rare_letter(list_name):
    letter = {}
    for name in list_name:
        for char in name:
            if char.isupper():
                letter[char] = letter.get(char, 0) + 1
            else:
                continue
    #print(type(letter), letter)
    letter_new = list(letter.items())
    #print(type(letter_new), letter_new)
    letter_new.sort(key=lambda i: i[0], reverse=True)
    #print(type(letter_new), letter_new)
    return letter_new[0][0]
print("Самая редкая буква: ", rare_letter(new_list_name))


'''
PRO
'''
print('Task_4: В файле с логами найти дату самого позднего лога (по метке времени)')
log_file_name = 'log.txt'
with open(log_file_name, 'r', encoding='utf-8') as text_file:
    max_date_str = ''
    for line in text_file:
        if line[:23] > max_date_str[:23]:
            max_date_str = line
print('Самая поздняя дата: ', max_date_str)




