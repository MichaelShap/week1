#SLOVARI

# my_dict = {}
# my_dict = dict()
# my_dict = {
#     'name': 'nazgul',
#     'age': 17,
#     'phone_number': '=996'
# }
# # print(my_dict['name'])
# # my_dict["car"] = 'prado' #добавили еще элемент в словарь
# # print(my_dict)
#
# # for i in my_dict:             #выводит первые значения
# #     print(i)
# #
# # for i in my_dict.items():      # выводит пары элементов - ключ и значение
# #     print(i)
#
# for i, y in my_dict.items():  # выводит пары элементов - ключ и значение
#     print(i, 'i')
#     print(y, 'y')

# my_dict = {}
# my_dict = dict()
# my_dict = {
#     'name': 'nazgul',
#     'age': 17,
#     'phone_numbers': {
#         'mega': '996',
#         'o': '312'},
#     'car': 'prado'
# }
# print(my_dict['phone_numbers'])
# my_dict['phone_numbers']['e-sim'] = '777'
# print(my_dict['phone_numbers'])

#ZADACHKA
# account = {
#     "usernames": [],
#     "emails": [],
#     "passwords":[],
# }
# username = input("vvedite imya polzovatelya: ")
# email = input("vvedite email: ")
# password = input("vvedite parol: ")
# valid_list = []
# if len(password) >= 8 and password.istitle():
#     valid_list.append(password)
# if email.endswith('@gmail.com') or \
#     email.endswith('@gmail.ru') or \
#     email.endswith('@outlook.com'):
#     valid_list.append(email)
# if len(valid_list) == 2:
#     account['usernames'].append(username)
#     account['emails'].append(valid_list[1])
#     account['passwords'].append(valid_list[0])
# print(account)
# #Ne rabotaiut drugie email


stop = True

db = {}

while stop:
    name = input('enter product: ')
    price  = input('enter product price: ')

    db[name] = price
    finish = input('do you want to stop: ')

    if finish.lower() == "yes":
        stop = False

        product_name = input('vvedite nazvanie producta: ')
        get_product_name = db.get(product_name)

        if get_product_name is None:
            print('producta net v baze')
        else:
            print(db[product_name])

print(db)

