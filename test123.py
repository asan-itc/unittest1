# 1) Находим минимальное положительное целое число, которого нет в списке. 
# Если список содержит только отрицательные числа, верните 1. 
# Все элементы являются целыми числами:
# Пример: [1,2,3,4,6] - Ответ 5
# Пример: [1,2,3] - Ответ 4
# Пример: [-1, -2, -6] - Ответ 1
# '''
# def sem(l):  
#     for i in range(1, max(l)):
#         if i not in  l:
#             return i
# print(sem([1,2,3,4,6])) 


# def som(a):
#     for x in range(1, len(a)+2):
#         if x not in a:
#             return x
# print(som([1,2,3]))


# def sam(l):
#     for i in range(1, len(l)+1):
#         if i not in  l:
#             return i
# print(sam([-1, -2, -6])) 

# """
# 2)Попросить пользователя ввести текст. В результате вывести процент букв 
# в верхнем регистре (заглавные) и в нижнем регистре (прописные).
# """

# def apalon(bot, spot):
#     return (sum(1 for x in bot if spot(x)) / len(bot))*100

# a = input()
# print( apalon( a, str.isupper ))
# print( apalon( a, str.islower ))

# """
# "3)Аналог шифра цезаря ". Программа должна запрашивать элементы списка через пробел. 
# После чего пользователь должен ввести значение для сдвига элементов списка. 
# Значение может быть как положительным, так и отрицательным. Если значение положительное, 
# элементы списка должны сдвигаться вправо, если отрицательное - влево. Результат необходимо вывести на экран:
# Введенные данные: [5,7,9,10,2], 2
# Результат:        [9,10,2,5,7]
# """

# spis = input('Input numbers:').split()
# b = []
# for i in spis:
#     b.append(int(i))
# com = int(input('Moving :'))
# print("Before-"+str(b)+', '+str(com))
# if com > 0:
#     b = b[com:]+b[:com]#Старт,стоп,шаг:СРЕЗЫ используется:list,str,tuple
#     print("After-",b)
# elif com < 0:
#     b = b[com:]+b[:com:]
#     print("After-",b)

# """
# "4)Напишите функцию которая принимает в себя словарь где ключи это номера а значения страны. Попросите пользователя ввести страну или ключ и выдайте ему результат."
# d = {'1': 'kyrgyzstan', '2': 'kazahstan'}
# """

# b = input("ведите ключ или страну: ")
# def c_k(k):
#     for key, value in k.items():
#         if key in b:
#             print(value)
#         if value in b:
#             print(key)
# c_k({'1': 'kyrgyzstan', '2': 'kazahstan'})


# """
# 5)'С помощью рекурсии выведите числа фибоначи'
# """

# def fibo(nachi):
#     if(nachi <= 1):
#         return nachi
#     else:
#         return (fibo(nachi -1) + fibo(nachi -2))

# nachi = int(input("введите число :"))

# print("вывод фибоначи с использованием рекурсии :")
# for iter in range(nachi):
#     print(fibo(iter))


# """
# 6)'С помощью рекурсии выведите факториал'
# # """
# def fac(x):
#     if x==0:
#         return 1
#     else:
#         return x*fac(x-1)
# a = int(input("Введите число: "))
# print (fac(a))



# """
# '7)С помощью рекурсии выполните перевод числа в двоичную систему счисления'
# "10 - 1010"
# "12 - 1100"
# "3 - 11"
# "15 - 1111""
# """
# def dwa(n):
#    if n > 1:
#        dwa(n//2)
#    print(n % 2,end = '')
# a = int(input("Введите число: "))
# dwa(a)
# print()


# """
# '8)Найдите длину списка при помощи рекурсии'
# """
# def len_r(lst):
#     if not lst:
#         return 0
#     return 1 + len_r(lst[1::2]) + len_r(lst[2::2])
# a = [ 2 , 7 , 3 , 9, 15, 35,] 
# print ( "Длина строка: " ) 
# print (len_r(a))
