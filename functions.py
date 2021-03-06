# Простейшая функция и описание
def add (x,y):
    '''
    :param x:
    :param y:
    :return:
    '''
    return x+y
help(add)  #просмотр описания функции

# Вызов функции
print(add(100,101))
print(add('Diana','+Kate'))

# Функция возвращает функцию
def f1(n):
    def f2(m):
        return n+m
    return f2
new_f = f1(100)
print(type(new_f), new_f)

new_f = f1(100)
print(new_f(250))

# Даже без return функция вернет None
def f():
    pass  # заглушка
print(f()) # None

# Аргументы функций
# Обязательные аргументы и не обязательные

def add (x,y,z=10):
    '''
    :param x:
    :param y:
    :return:
    '''
    return x+y+z
print(add(1,2)) # 13
print(add(1,2,3)) #6

# args
def func (*args):
    print(type(args), args)
    return args
func(1,2,3,'Volvo') # кортеж

# kwargs
def func (**kwargs):
    print(type(kwargs), kwargs)
    return kwargs
func(a=1,b=2,c='Volvo',d=1.2) # словарь

# Все вместе
def func_dificult (x,y=2,*args,**kwargs):
    print(type(x), x)
    print(type(y), y)
    print(type(*args), *args)
    print(type(kwargs), kwargs)
    return kwargs
func_dificult(1,3, (1,2,3), temp = 12, temp_1 = 13) # вызываем с одним обязательным параметром
