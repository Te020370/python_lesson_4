def ident(x):
    return x
print(ident(10))

# тоже самое
print((lambda x: x) (10))

# определение функции
ident_lambda = lambda x: x
print(ident_lambda(10))

car = lambda brend, engiту_volume, price: f'Car = {brend.title()}, Engine_volume = {engiту_volume}, Price = {price}'
print(car('Volvo', 1.5, 1300000))
print(type(ident_lambda), type(ident))
