"""Задача 1"""


class Date:
    def __init__(self, date=str):
        self.date = date

    @classmethod
    def date_usual(cls, date=str):
        day, month, year = date.split()
        return f'{day}.{month}.{year}'

    @staticmethod
    def is_valid(date=str):
        try:
            day, month, year = date.split()
            if int(day) not in range(1, 32):
                raise ValueError('День не входит в интервал [1;31]')
            elif int(month) not in range(1, 13):
                raise ValueError('Месяц не входит в интервал [1;13]')
        except ValueError as e:
            print(e)
        else:
            print('Дата верна')


date_1 = Date('01 01 2022')
print(date_1.date_usual('01 01 2022'))
print(Date.date_usual('07 02 2022'))
print(date_1.is_valid('01 01 2022'))
print(Date.is_valid('01 01 2022'))


"""Задача 2"""


class DivEr(Exception):
    def __init__(self, message):
        self.message = message


while True:
    dividend = float(input('Ввод делимого: '))
    divider = float(input('Ввод делителя: '))
    try:
        if divider == 0:
            raise DivEr('Деление на 0')
        result = dividend / divider
        print(result)
    except DivEr as error:
        print(error)


"""Задача 3"""


class ListDigitCheck(Exception):
    def __init__(self):
        print('Список некорректен')

def check(input_string=str):
    try:
        if not input_string.isdigit():
            raise ListDigitCheck
    except ListDigitCheck as error:
        print(error)
    else:
        return True


my_list = []
while True:
    string = input('Введите строку: ')
    if not string:
        break
    if check(string):
        my_list.append(string)
print(my_list)


"""Задачи 4-6"""
"""Если честно, не уверен что правильно понял условия заданий, так что сделал как сделал (разбор решил не смотреть,
чтоб ничего не подглядеть). Хотел еще добавить кучу методов, вроде подсчета оставшихся не занятых мест на складе,
но пора бы уже сдать это дз.
 Задачу 6 по проверке вводимых данных реализовал в методе sub класса склад, правда, не исключением, а условием:
 там я проверяю, есть ли вообще то что пользователь ввел в данный момент на складе. Еще не уверен, что переменную
 _subdivisions стоит делать переменной класса, объявляемой не при инициализации, но уже сделал так"""

class Warehouse:
    _subdivisions = {'s1': [], 's2': [], 's3': []}

    def __init__(self, place, objects=dict):
        self.__place = place
        self.__objects = objects
        print(f'На складе {self.__place} мест')

    def sub(self, object, sub=str):
        if self.__objects[object]:
            Warehouse._subdivisions[sub].append(object)
        else:
            print('Такого на складе нет')
        print(f'Теперь {object} в подразделении {sub}')

    @property
    def place(self):
        return f'Сейчас на складе {self.__place} мест'

    @place.setter
    def place(self, number):
        self.__place = number
        print(f'Теперь на складе {self.__place} мест')

    @property
    def objects(self):
        return f'Склад содержит: {self.__objects}'

    @objects.setter
    def objects(self, new_objects=dict):
        add = input('Добавить объект или заменить на него все остальные? ')
        if add == 'Добавить':
            self.__objects.update(new_objects)
        else:
            self.__objects = new_objects
        print(f'Теперь склад содержит {self.__objects}')


class Device:
    def __init__(self, params=dict):
        self.__params = params
        print(f'Это {self.__params.get("Название")}')


class Printer(Device):
    def __init__(self, params=dict, unique_param=str):
        super().__init__(params)
        self.__params = params
        self.__printSpeed = unique_param
        self.__params.update({'Скорость печати': unique_param})

    def __str__(self):
        if "Название" in self.__params.keys():
            return f'принтер "{self.__params["Название"]}"'
        else:
            return f'Принтер, название которого вы только что стерли'

    def __repr__(self):
        if "Название" in self.__params.keys():
            return f'принтер "{self.__params["Название"]}"'
        else:
            return f'Принтер, название которого вы только что стерли'

    @property
    def params(self):
        return f'Параметры устройства: ' \
               f'{self.__params}'

    @params.setter
    def params(self, new_params=dict):
        add = input('Добавить параметр или заменить на него все остальное? ')
        if add == 'Добавить':
            self.__params.update(new_params)
        else:
            self.__params = new_params
        print(f'Теперь параметры устройства: {self.__params}')


class Scanner(Device):
    def __init__(self, params=dict, unique_param=dict):
        super().__init__(params)
        self.__params = params
        self.__resolution = unique_param
        self.__params.update({'Разрешение': unique_param})

    def __str__(self):
        if "Название" in self.__params.keys():
            return f'сканер "{self.__params["Название"]}"'
        else:
            return f'сканер, название которого вы только что стерли'

    def __repr__(self):
        if "Название" in self.__params.keys():
            return f'принтер "{self.__params["Название"]}"'
        else:
            return f'Принтер, название которого вы только что стерли'

    @property
    def params(self):
        return f'Параметры устройства: ' \
               f'{self.__params}'

    @params.setter
    def params(self, new_params=dict):
        add = input('Добавить параметр или заменить на него все остальное? ')
        if add == 'Добавить':
            self.__params.update(new_params)
        else:
            self.__params = new_params
        print(f'Теперь параметры устройства: {self.__params}')

class Xerox(Device):
    def __init__(self, params=dict, unique_param=dict):
        super().__init__(params)
        self.__params = params
        self.__resolution = unique_param
        self.__params.update({'Скорость копирования': unique_param})

    def __str__(self):
        if "Название" in self.__params.keys():
            return f'копировальная машина "{self.__params["Название"]}"'
        else:
            return f'копировальная машина, название которой вы только что стерли'

    def __repr__(self):
        if "Название" in self.__params.keys():
            return f'копировальная машина "{self.__params["Название"]}"'
        else:
            return f'копировальная машина, название которой вы только что стерли'

    @property
    def params(self):
        return f'Параметры устройства: ' \
               f'{self.__params}'

    @params.setter
    def params(self, new_params=dict):
        add = input('Добавить параметр или заменить на него все остальное? ')
        if add == 'Добавить':
            self.__params.update(new_params)
        else:
            self.__params = new_params
        print(f'Теперь параметры устройства: {self.__params}')


p = Printer({'Название': 'printer_1', 'Год выпуска': '2021', 'Модель': 'p_model_1', 'Цена': '100'},  '6 листов в минуту')
print(p.params)
p.params = {'Масса': '3 кг'}

s = Scanner({'Название': 'scanner_1', 'Год выпуска': '2020', 'Модель': 's_model_1', 'Цена': '150'},  '600 dpi')
print(s.params)

x = Xerox({'Название': 'copy_machine_1', 'Год выпуска': '2021', 'Модель': 'cm_model_1', 'Цена': '50'})

w = Warehouse(10, {s: 1, p: 1, x: 2})
w.sub(s, 's1')
print(Warehouse._subdivisions)
w.sub(p, 's1')
print(Warehouse._subdivisions)
w.sub(x, 's2')
print(Warehouse._subdivisions)


"""Задача 7"""


class ComplexDigit:
    def __init__(self, a, b):
        self.Re = a
        self.Im = b

    def __str__(self):
        return f'{self.Re} + i*{self.Im}'

    def __add__(self, other):
        a = self.Re + other.Re
        b = self.Im + other.Im
        return ComplexDigit(a, b)

    def __mul__(self, other):
        a = self.Re * other.Re - self.Im * other.Im
        b = self.Im * other.Re + self.Re * other.Im
        return ComplexDigit(a, b)


x = ComplexDigit(1, 4)
y = ComplexDigit(3, 2)
z = x + y
print(z)
w = x * y
print(w)
t = z + w
print(t)
