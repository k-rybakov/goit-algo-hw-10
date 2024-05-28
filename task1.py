from pulp import LpMaximize, LpProblem, LpVariable

# Створення проблеми
problem = LpProblem("Maximize_Production", LpMaximize)

# Змінні
x1 = LpVariable("Lemonade", lowBound=0, cat="Integer")
x2 = LpVariable("Fruit_Juice", lowBound=0, cat="Integer")

# Об'єктивна функція
problem += x1 + x2, "Total_Products"

# Обмеження
problem += 2 * x1 + 1 * x2 <= 100, "Water_Constraint"
problem += 1 * x1 <= 50, "Sugar_Constraint"
problem += 1 * x1 <= 30, "Lemon_Juice_Constraint"
problem += 2 * x2 <= 40, "Fruit_Puree_Constraint"

problem.solve()

print(f"Лимонад : {x1.varValue}") # 30
print(f"Фруктовий сік : {x2.varValue}") # 20
