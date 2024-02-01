import random
import scipy.integrate as spi

# Розміри прямокутника
a = 2  # ширина прямокутника
b = 4  # висота прямокутника


def is_inside(a, b, x, y):
    """Перевіряє, чи знаходиться точка (x, y) всередині трикутника."""
    return y <= x**2


def monte_c(counter=0, SmPrev=0, points=[]):
    """Рахує площу фігури, після чого перевіряє рівень змін в порівнянні з попреедньою ітерацією. При невиконанні бажаних умов, запускається рекурсивно"""
    counter += 1
    points.extend([(random.uniform(0, a), random.uniform(0, b)) for _ in range(1000)])
    inside_points = [point for point in points if is_inside(a, b, point[0], point[1])]

    N = len(points)
    M = len(inside_points)
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

with open("readme.md", "w", encoding="utf-8") as fp:
    fp.writelines(
        "Модель була змінена таким чином. Раунд додає 1000 точок у площину.\nВираховується площа. Якщо площа від попередньої ітерації відрізняється менше ніж задане число (в данному випадку 0.0001), тоді модель зупиняється, вважаючи що бажана точність досягнута.\n"
    )
    fp.writelines(f"Теоретична площа фігури: {S}, площа за методом Монте-Карло: {Sm}\n")
    fp.writelines(
        f"Точність до 0,00001 була досягнута за {rounds} раундів, кожен по 1000 точок.\n"
    )
