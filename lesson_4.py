# num1 = 6
# num2 = 5
# if num1 > num2:
#     print(num2 + num1)
#
#
# num1 = 6
# num2 = 5
# if num1 > num2:
#     print(num2 + num1)
#
#  if
# # num1 = 6
# num2 = 5
# if num1 > num2 and num2 == 9:
#     print(num2 + num1)
# elif num2 > num1:
#     print(num1 - num2)
# else:
#     print("the end")
# if num1 > num2 or num2 == 9:
#     print(num2 + num1)

# number_1 = int(input("Vvedite 1 oe chislo: "))
# number_2 = int(input("Vvedite 2 oe chislo: "))
# oper = input("Vvedite operator: ")
# if oper == "+":
#     print(number_1 + number_2)
# elif oper == "-":
#     print(number_1 - number_2)
# elif oper == "*":
#     print(number_1 * number_2)
# elif oper == "/":
#     print(number_1 / number_2)
# else:
#     print("operator not found!")
#

# number = float(input("Vvedite znachenie temperatury: "))
# ed = str(input("Vvedite znachenie temperatury C or F: "))
# if ed  == 'C':
#         print((number * 9/5) + 32)
# elif ed == 'F':
#         print((number - 32) * 5/9)
# else:
#         print('Nevernoe znachenie edinici izmereniya')
#
#

# temp = float(input("Vvedite znachenie temperatury v C: "))
# if temp  < -273.15:
#         print('temperatura nedeistvitelna')
# elif temp  == -273.15:
#         print('temperatura ravna absolutnomu nolu')
# elif temp  > -273.15 and temp < 0:
#         print('temperatura nije tochki zamerzania')
# elif temp  == 0:
#         print('temperatura v tochke zamerzania')
# elif temp  > 0 and temp < 100:
#         print('temperatura v norm diapazone')
# elif temp  == 100:
#         print('temperatura v tochke kipenia')
# elif temp  > 100:
#         print('temperatura vishe tochki kipenia')


#list
# my_list = [1, 2, 3, 'Andrei', [1, '67']]
# my_list[2] = 'Nurzada'
# print(my_list)
# print(my_list[3:])
# print(my_list[3:-1])
# print(my_list[-1])
# print(my_list[-1][0]) #вложенный массив, сделали срез, и ндекс нужного числа во втором массиве

# my_list = []
# my_list = list()
#создали пустой лист, 2 способа

#берет каждый элемент из май лист, пока не закончатся
# my_list = [1, 2, 3, 'Andrei', [1, '67']]
# for i in my_list:
#     print(i)
#     if type(i) == str:
#         print(i.upper())

#
my_list = []
my_list.append(4)
my_list.append(3)
print(my_list)
print(my_list.append(3))

# my_list = [1, 3, 4, 5, 6,]
# print(my_list + [2,3,])
#
# my_list.extend(['mfb', 'fejbe'])
# print(my_list)

# my_list.insert(3, 'Nazgul')
# print(my_list)
# my_list.reverse()
# print(my_list)

# my_list = [3, 4, 5, 6, 4, 2]
# my_list.sort()
# print(my_list)

# str_list = ['Aff', 'b', 'c', 'Ca' ]
# str_list.sort(key=len)
# print(str_list)

# phones = ['996555443322', '996777665544']
# # black_phone = phones.pop(1)
# # print(phones)
# # print(black_phone)
# # phones.remove('996777665544')
# print(phones)
# print(phones.count('996777665544'))
# print(phones.index('996777665544'))