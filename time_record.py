import timeit, time
# code_to_test = """
# a = range(100000)
# b = []
# for i in a:
#     b.append(i*2)
# """

# elapsed_time =  timeit.timeit(code_to_test, number=100)/100
# print(elapsed_time)

def dict_method():
    
    scrab = {'A': '1', 'E': '1', 'I': '1', 'O': '1', 'U': '1', 'L': '1', 'N': '1', 'S': '1', 'T': '1', 'R': '1', 'А': '1', 'В': '1', 'Е': '1', 'И': '1', 'Н': '1', 'О': '1', 'Р': '1', 'С': '1', 'Т': '1',
            'D': '2', 'G': '2', 'Д': '2', 'К': '2', 'Л': '2', 'М': '2', 'П': '2', 'У': '2',
            'B': '3', 'C': '3', 'M': '3', 'P': '3', 'Б': '3', 'Г': '3', 'Ё': '3', 'Ь': '3', 'Я': '3',
            'F': '4', 'H': '4', 'V': '4', 'W': '4', 'Y': '4', 'Й': '4', 'Ы': '4',
            'K': '5', 'Ж': '5', 'З': '5', 'Х': '5', 'Ц': '5', 'Ч': '5',
            'J': '8', 'X': '8', 'Ш': '8', 'Э': '8', 'Ю': '8',
            'Q': '10', 'Z': '10', 'Ф': '10', 'Щ': '10', 'Ъ': '10'}

    #word = str(input('Введите слово на английском или русском языке: ')).upper()
    word = ('ноутбук').upper()
    print(word)
    summary = 0
    for char in word:
        summary += int(scrab[char])

    print(f'Стоимость этого слова - {summary}')
    return summary

def list_met():
    
    list_1 = [1,"а","в","е","и","н","о","р","с","т"]
    list_2 = [2,"д","к","л","м","п","у"]
    list_3 = [3,'б', 'г', 'ё', 'ь', 'я']
    list_4 = [4, "ы"]
    list_5 = [5,"ж","з","х","ц","ч"]
    list_8 = [8,"ш","э","ю"]
    list_10 = [10,"ф","щ","ъ"]

    gen_list = [list_1,list_2,list_3,list_4,list_5,list_8,list_10]

    summa = 0
    #word = input("Введите слово: ")
    word = ('ноутбук').lower()
    
    #print()
    for i in range(len(word)):
        for el in gen_list:
            if word[i] in el:
                summa  += el[0]
                    
    print(f'сумма = {summa}')
    return summa

def main():
    
    start_time = time.time()
    for i in range(1001):
        dict_method()
    
    #print("--- %s seconds ---" % (time.time() - start_time))
    final_1 = "--- %s seconds ---" % (time.time() - start_time)

    
    start_time = time.time()
    for i in range(1001):
        list_met()
    
    #print("--- %s seconds ---" % (time.time() - start_time))
    final_2 = "--- %s seconds ---" % (time.time() - start_time)

    print("===== СЛОВАРЬ =================" )
    print(final_1)
    print()
    print("===== СПИСОК =================" )
    print(final_2)
    print()
   
main()


# start_time = time.time()
# main()
# print("--- %s seconds ---" % (time.time() - start_time))