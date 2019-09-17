
input_array = [2, 4, 6, 8, 10,12,12]

def iter_function(input_array):
    even_obj=iter(input_array)
    print(next(even_obj))
    print(next(even_obj))
    print(next(even_obj))
    print(next(even_obj))
    print(next(even_obj))
    print(next(even_obj))
    print(next(even_obj))
    print(next(even_obj))


print(iter_function(input_array))