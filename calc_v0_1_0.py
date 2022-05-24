import re
from math import trunc
from types import NoneType
from my_math import sum, sub, mul, div
# from my_print import *
from my_find import *

# PAUSE = False

def recurs(sub_expr):
    # system_pause(PAUSE)
    print('1)', sub_expr)
    left_skobka, right_skobka = find_skobki(sub_expr)
    print('2)----\n', type(left_skobka), left_skobka, right_skobka)
    while left_skobka != -1: 
        print('3)')
        skob_part = sub_expr[left_skobka : right_skobka+1]
        print('4)', skob_part)
        print('5)', skob_part[1 : len(skob_part)-1])
        sub_expr = sub_expr.replace(skob_part, recurs(skob_part[1 : len(skob_part)-1])) 
        left_skobka, right_skobka = find_skobki(sub_expr)




    print('скобок нет', sub_expr)  
    while(1):
        # print(test2)
        mini_expr = re.search(r"[.\d]{0,}\*[.\d]{0,}", sub_expr)
        if type(mini_expr) == NoneType:
            print("Умножений нет", type(mini_expr))
        else:
            sub_expr = sub_expr.replace(str(mini_expr.group()), str(mul(mini_expr.group())))
            continue

        mini_expr = re.search(r"[.\d]{0,}\/[.\d]{0,}", sub_expr)
        if type(mini_expr) == NoneType:
            print("Делений нет", type(mini_expr))
        else:
            sub_expr = sub_expr.replace(str(mini_expr.group()), str(div(mini_expr.group())))
            continue
        
        mini_expr = re.search(r"[.\d]{0,}\+[.\d]{0,}", sub_expr)
        if type(mini_expr) == NoneType:
            print("Сложений нет", type(mini_expr))
        else:
            sub_expr = sub_expr.replace(str(mini_expr.group()), str(sum(mini_expr.group())))
            continue
        # было r"\d{0,}\-\d{0,}"
        mini_expr = re.search(r"[.\d]{0,}\-[.\d]{0,}", sub_expr)
        if type(mini_expr) == NoneType:
            print("Вычитаний нет", type(mini_expr))
        else:
            sub_expr = sub_expr.replace(str(mini_expr.group()), str(sub(mini_expr.group())))
            continue
        break
    print(sub_expr)
    return sub_expr

        
    




# expr = input("Введите выражение: ")
# print(expr)

# result = float(recurs(expr))

# print("Начальное выражение:", expr)

# if result == trunc(result):
#     print("\nРезультат:", trunc(result))
# else:
#     print("\nРезультат:", result)
