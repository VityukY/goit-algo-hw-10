"""
Умови завдання:

"Лимонад" виготовляється з "Води", "Цукру" та "Лимонного соку".
"Фруктовий сік" виготовляється з "Фруктового пюре" та "Води".
Обмеження ресурсів: 100 од. "Води", 50 од. "Цукру", 30 од. "Лимонного соку" та 40 од. "Фруктового пюре".
Виробництво одиниці "Лимонаду" вимагає 2 од. "Води", 1 од. "Цукру" та 1 од. "Лимонного соку".
Виробництво одиниці "Фруктового соку" вимагає 2 од. "Фруктового пюре" та 1 од. "Води".

 "Лимонаду" та "Фруктового соку" 
"""
import pulp


# Ініціалізація моделі
model = pulp.LpProblem("Maximize Profit", pulp.LpMaximize)

# Визначення змінних
lemononade = pulp.LpVariable(
    "Lemonade", lowBound=0, cat="Integer"
)  # Кількість продукту 1
fruit_juice = pulp.LpVariable(
    "Fruit juice", lowBound=0, cat="Integer"
)  # Кількість продукту 2


# Функція цілі (Максимізація прибутку)
model += lemononade + fruit_juice, "Profit"


# Додавання обмежень
model += 2 * lemononade + fruit_juice <= 100, "Constraint1"
model += lemononade <= 50, "Constraint2"
model += lemononade <= 30, "Constraint3"
model += fruit_juice <= 40, "Constraint4"


# Розв'язання моделі
model.solve()
print(pulp.LpStatus[model.status])

for variable in model.variables():
    print(f"{variable.name} = {variable.varValue}")
# Вивід результатів
print("Виробляти продуктів лимонаду:", lemononade.varValue)
print("Виробляти продуктів фруктового соку:", fruit_juice.varValue)
