# def line():
#     print('-' * 30)

# line()
# print('   TESTE   ')
# line()
# print('   PYTHON   ')   
# line()
# print('   GABRIEL MINATTO   ')
# line()

# def msg(txt):
#     print('-' * 30)
#     print(txt)
#     print('-' * 30)

# msg('GABRIEL MINATTO')

# def sum(a, b):
#     s = a + b
#     print(s)
    

# sum(4, 5)
# sum(6, 7)
# sum(7, 8)

def counter(* num):
    tam = len(num)
    print(f'recebi os valores {num} e são ao todo {tam} números.')


counter(2, 1, 7)
counter(8, 0)
counter(4, 4, 7, 6, 2)


# def doble(lst):
#     pos = 0 
#     while  pos < len(lst):
#         lst[pos] *= 2
#         pos += 1

# values = [7, 2, 5, 0, 4]
# doble(values)
# print(values)