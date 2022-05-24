import re

def sum(mini):
    sign = re.search(r"\+", mini)
    index = mini.find(sign.group())
    left = mini[ : index]
    right = mini[index+1 : ]
    if mini[ : index] == '':
        left = 0
    if mini[index+1 : ] == '':
        right = 0
    res = float(left) + float(right)
    print(res)
    return res

def sub(mini):
    sign = re.search(r"-", mini)
    index = mini.find(sign.group())
    left = mini[ : index]
    right = mini[index+1 : ]
    if mini[ : index] == '':
        left = 0
    if mini[index+1 : ] == '':
        right = 0
    res = float(left) - float(right)
    print(res)
    return res

def mul(mini):
    sign = re.search(r"\*", mini)
    index = mini.find(sign.group())
    left = mini[ : index]
    right = mini[index+1 : ]
    if mini[ : index] == '':
        left = 0
    if mini[index+1 : ] == '':
        right = 0
    res = float(left) * float(right)
    print(res)
    return res

def div(mini):
    sign = re.search(r"/", mini)
    index = mini.find(sign.group())
    left = mini[ : index]
    right = mini[index+1 : ]
    if mini[ : index] == '':
        left = 0
    if mini[index+1 : ] == '':
        right = 0
    try:
        res = float(left) / float(right)
    except:
        print("Деление на ноль!")
        exit
    else:
        print(res)
        return res

