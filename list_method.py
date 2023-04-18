print()
list_1 = [1,"а","в","е","и","н","о","р","с","т"]
list_2 = [2,"д","к","л","м","п","у"]
list_3 = [3,'б', 'г', 'ё', 'ь', 'я']
list_4 = [4, "ы"]
list_5 = [5,"ж","з","х","ц","ч"]
list_8 = [8,"ш","э","ю"]
list_10 = [10,"ф","щ","ъ"]

gen_list = [list_1,list_2,list_3,list_4,list_5,list_8,list_10]

summa = 0
word = input("Введите слово: ")
print()
for i in range(len(word)):
    for el in gen_list:
        if word[i] in el:
            summa  += el[0]
            
print(f'сумма = {summa}')
print()
