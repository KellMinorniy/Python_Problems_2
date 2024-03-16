import random

def circle_sqake_mk(r, n):
    points_inside = 0
    for _ in range(n):
        x = random.uniform(-r, r)
        y = random.uniform(-r, r)
        if x**2 + y**2 <= r**2:
            points_inside += 1
    return (points_inside / n) * (4 * r**2)

r = 5 
n = 100000

mk_area = circle_sqake_mk(r, n)
print(f"Площадь окружности методом Монте-Карло: {mk_area}")

formula_area = 3.14159 * r**2
print(f"Площадь окружности по формуле: {formula_area}")

mk_error = abs(mk_area - formula_area) / formula_area * 100
print(f"Погрешность метода Монте-Карло: {mk_error}%")