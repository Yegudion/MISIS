import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Определение данных
X = np.array([1, 2, 3, 4, 5, 6, 7])
Y = np.array([35.07, 34.08, 31.80, 30.44, 27.97, 25.15, 22.14])

# Создание датафрейма
data = pd.DataFrame({'X': X, 'Y': Y})

# Добавление квадратичного члена к X
X2 = X**2

# Объединение X и X2
X = sm.add_constant(np.column_stack((X, X2)))

# Обучение модели
model = sm.OLS(Y, X).fit()

# Печать результатов
print(model.summary())

# Получение предсказанных значений
y_pred = model.predict(X)

# Построение графика рассеяния и линии регрессии
plt.scatter(X[:,1], Y)
plt.plot(X[:,1], y_pred, color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('График регрессии')
plt.show()

# F-тест
f_statistic, p_value = model.f_test().fvalue, model.f_test().pvalue

# Вывод результатов
print(f"F-статистика: {f_statistic}")
print(f"p-значение: {p_value}")
