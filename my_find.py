def find_skobki(sub_expr):
    print('\n0_', sub_expr)
    try:
        start = sub_expr.index('(')
    except:
        return -1, -1
    if start == -1:
        print("1_")
        return -1, -1
    else:
        print('2_', start)
        counter = 0
        print('3_', sub_expr[start+1 : ])
        for i, ch in enumerate(str(sub_expr[start+1 : ])):
            if ch == '(':
                print('q', i, ch, counter)
                counter += 1
            elif ch == ')' and counter != 0:
                print('e', i, ch, counter)
                counter -= 1
            elif ch == ')' and counter == 0:
                print('4_', start, i)
                return start, start+(i+1)
            
