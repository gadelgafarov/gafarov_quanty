# # # def build_qeury_string(base_url, **kwarks):
# # #     args = []

# # #     args_list = list(kwarks.items())
# # #     for arg in args_list:
# # #         str_arg = f'{arg[0]}={arg[1]}'
# # #         args.append(str_arg)
# # #     result = base_url + '?' + '&'.join(args)
# # #     return result


# # # print(build_qeury_string('https://api.weather.com/v1/forecast', city = 'Moscow', days=3, units='metric'))


# # catalog = [
# #     {'name':'Смартфон', 'price': 45000, 'rating': 4.8},
# #     {'name':'Чехол для телефона', 'price': 500, 'rating': 4.2},
# #     {'name':'Беспроводные наушники', 'price': 7000, 'rating': 4.8},
# #     {'name':'Зарядное устройство', 'price': 1200, 'rating': 4.5}
# # ]


# # result = sorted(
# #     catalog,
# #     key=lambda item: item['price']
# # )
# # print("Сортировка по цене (возрастание)")
# # for item in result:
# #     print(item['name'], f'({item["price"]} руб.)')
# # print()
# # print("Сортировка по рейтингу (убывание) и цене (возрастание)")
# # result = sorted(
# #     result,
# #     key=lambda item: item['rating'],
# #     reverse=True
# # )
# # for item in result:
# #     print(item['name'], f'({item["rating"]}', f', {item["price"]} руб.)')




# # class Animal:
# #     def __init__(self, color, name):
# #         self.color = color
# #         self.name = name
    
# #     def make_sound(self):
# #         print("I am an animal")

# # animal = Animal('blue', 'barsik')
# # animal.make_sound()


# # class Dog(Animal):
# #     def __init__(self, color, name, master):
# #         Animal.__init__(self, color, name)
# #         self.master = master
    

# #     def make_sound(self):
# #         print('bark')
# # dog = Dog('brown', 'Persik', 'I')
# # dog.make_sound()


# # class Cat(Animal):
# #     def __init__(self, color, name, master, lifes):
# #         Animal.__init__(self, color, name)
# #         self.lifes = lifes


# #     def make_sound(self):
# #         print('Myr')
# # cat = Cat('black', 'Shunshun', 'Steve', '9')
# # cat.make_sound()


# class Transport:
#     def __init__(self, nickname, speed):
#         self.nickname = nickname
#         self.speed = speed

#     def max_speed():
#         print('More than one')


# transport = Transport('machine', 'a lot  of')
# transport.max_speed()


# class F1(Transport):
#     def __init__(self, nickname, speed, size):
#         super().__init__(nickname, speed)
#         self.size = size


#     def max_speed():
#         print('more than 300')


# ferrari = F1('ferrari' , '300' , 'small')


print('New World')