# map
name = ['Мaша', 'Петя','Михаил']
name_lengths = list(map(len, name))
print(type(name_lengths), name_lengths) # => [4,4,6]
print(name_lengths)

squares = list(map(lambda x: x * x, [0,1,2,3,4]))
print(type(squares), squares)

def miles_to_km(miles):
    return miles*1.6
miles_dist = [1.0, 1.6, 2.3]
km_dist = list(map(miles_to_km, miles_dist))
print(type(km_dist), km_dist)


km_dist = list(map(lambda x: 1.6*x, miles_dist))
print(type(km_dist), km_dist)

list_1 = [1,2,3]
list_2 = [4,5,6]
list_3 = list(map(lambda x,y: x+y, list_1, list_2))
print(type(list_3), list_3)



# reduce
from functools import reduce # начиная с 3...

sum_all = reduce(lambda x,y: x+y, [1,2,3,4,5])
print(sum_all)

list_temp = [43,12,41,100,101,4]
max = reduce(lambda a,b: a if a > b else b,list_temp)
print(max)

# filter

list_50 = list(filter(lambda x: x > 50,list_temp))
print(list_50)

list_10 = list(filter(lambda x: x %10 == 1,list_temp))
print(list_10)

# sort

list_temp_sort = sorted(list_temp)
print(list_temp_sort)

list_temp_sort_reverse = sorted(list_temp_sort, reverse=True)
print(list_temp_sort_reverse)

# KEY

list_name = ['Kate', 'Ivan', 'Dima', 'Mike']
list_name_sort = sorted(list_name)
print(list_name_sort)

list_name_sort_key = sorted(list_name, key = lambda x: x[1])
print(list_name_sort_key)
