# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the -sea shore The -shells
# that she -sells are -sea -shells I'm sure.So if -she -sells -sea
# -shells -on -the -sea -shore I'm sure -that -the -shells -are -sea
# -shore -shells
# Output: 13
import re

print()

inp_str = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"

inp_str = inp_str.lower()
print('получено: ', inp_str)
#inp_list = inp_str.split()
#inp_list = inp_str.split('.')
#inp_list = inp_str.split("'")
inp_list = re.split(" . | ' | , ", inp_str)
print('обработано: ', inp_list)
dict = {}
for i in range(len(inp_list)):
    print(inp_list[i])
    if inp_list[i] in dict:
        dict[inp_list[i]] += 1
    else:
        dict[inp_list[i]] = 1
    #print('{} : {}'.format(i, dict[i]))    
for i in dict:
    print('{} : {}'.format(i, dict[i]))
#print(end = '\n')
print(len(dict))
