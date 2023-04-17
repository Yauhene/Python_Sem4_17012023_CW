# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

print()
first_str = 'a a a b c a a d c d d'
list_str = list(first_str.split())
print(first_str)
my_dict = {}

for i in range(len(list_str)):
    if list_str[i] in my_dict:
        my_dict[list_str[i]] += 1
        list_str[i] += '_' + str(my_dict[list_str[i]])
    else:
        my_dict[list_str[i]] = 1
        list_str[i] += '_' + str(my_dict[list_str[i]])
        
print('--------------------------------------------')
for i in range(len(list_str)):
    print(list_str[i], end = " ")
print( end = '\n')
print('--------------------------------------------')
print()



