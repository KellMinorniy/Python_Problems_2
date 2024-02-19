import time
import timeit

def fact_rec(n):
    if n ==  0 or n ==  1:
        return  1
    else:
        return n * fact_rec(n -  1)

def fact_it(n):
    result =  1
    for i in range(1, n +  1):
        result *= i
    return result

rec_time = timeit.timeit(lambda: fact_rec(5), number=1)
print("Время рекурсивной функции:", rec_time)

it_time = timeit.timeit(lambda: fact_it(5), number=1)
print("Время итерационной функции:", it_time)

print(rec_time / it_time)