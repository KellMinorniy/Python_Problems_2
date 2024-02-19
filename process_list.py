import timeit

def process_list_lc(arr):
    return [i**2 if i %   2 ==   0 else i**3 for i in arr]

def process_list_gen(arr):
    for i in arr:
        yield i**2 if i %   2 ==   0 else i**3

arr = list(range(1,   10**3 +   1))

# Время list comprehension
start_time = timeit.default_timer()
process_list_lc(arr)
elapsed_time_lc = timeit.default_timer() - start_time

# Время функции-генератора
start_time = timeit.default_timer()
list(process_list_gen(arr))
elapsed_time_gen = timeit.default_timer() - start_time

print(f"Время list comprehension {elapsed_time_lc} секунд")
print(f"Время функции-генератора: {elapsed_time_gen} секунд")

# list comprehension быстрее функции-генератора