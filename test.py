from pulp import LpProblem, LpMaximize, LpVariable

# Створення об'єкту задачі для максимізації
model = LpProblem(name="Beverage_Production", sense=LpMaximize)

# Оголошення змінних рішення (кількість "Лимонаду" та "Фруктового соку")
x = LpVariable(name="Lemonade_units", lowBound=0, cat="Integer")
y = LpVariable(name="Fruit_juice_units", lowBound=0, cat="Integer")

# Додавання обмежень
model += 2 * x + y <= 100, "Water_constraint"
model += x <= 50, "Sugar_constraint"
model += x <= 30, "Lemon_juice_constraint"
model += 2 * y <= 40, "Fruit_puree_constraint"

# Додавання функції максимізації (припустима функція прибутку)
model += x + y, "Maximize_Profit"

# Вирішення задачі
model.solve()

# Виведення результатів
print(f"Optimal units of Lemonade: {int(x.value())}")
print(f"Optimal units of Fruit Juice: {int(y.value())}")
print(f"Maximum Profit: ${model.objective.value()}")
