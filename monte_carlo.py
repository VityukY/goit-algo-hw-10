import random
import scipy.integrate as spi

# Розміри прямокутника
a = 2  # ширина прямокутника
b = 4  # висота прямокутника


def is_inside(a, b, x, y):
    """Перевіряє, чи знаходиться точка (x, y) всередині трикутника."""
    return y <= x**2


def monte_c(counter=0, SmPrev=0, points=[]):
    counter += 1
    print(counter)
    points.extend([(random.uniform(0, a), random.uniform(0, b)) for _ in range(1000)])
    inside_points = [point for point in points if is_inside(a, b, point[0], point[1])]

    N = len(points)
    M = len(inside_points)
    print(N)
    print(M)
    SmCurrent = (M / N) * (a * b)  # Площа за методом Монте-Карло
    if SmCurrent - SmPrev > 0.00001 or SmCurrent - SmPrev < -(0.00001):
        return monte_c(counter, SmCurrent, points)
    else:
        return (SmCurrent, counter)


Sm, rounds = monte_c()


# Теоретична площа трикутника та площа, обчислена методом Монте-Карло
def f(x):
    return x**2


S = result, error = spi.quad(f, 0, 2)  # Теоретична площа

# Виведення результатів, зміненої моделі
print(f"Теоретична площа фігури: {S}, площа за методом Монте-Карло: {Sm}")
print(f"Точність до 0,00001 була досягнута за {rounds} раундів, кожен по 1000 точок.")
