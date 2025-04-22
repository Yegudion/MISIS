from collections import defaultdict
import matplotlib.pyplot as plt
import math

# Функция для вычисления среднего значения
def mean(arr: list[int]):
    return sum(arr) / len(arr)



lines = open("/home/yegor/my_data/MISIS_LABS/5 семестр/Методы статистического анализа данных /lab1/Москва_2021.txt", "r")
lines = list(map(int, lines))
lines = list(map(int, lines))
freq = defaultdict(int)
for num in lines:
    freq[num] += 1


xs = []
ys = []
data = []

for k, v in sorted(freq.items()):
    print(f"{k}: {v}")
    xs.append(k)
    ys.append(v)
    data.append((k, v))

plt.bar(xs, ys)
plt.show()




print(mean(lines))

# Вычисление квадратов каждого значения и их сортировка
squares = [x ** 2 for x in lines]
squares.sort()

# Вычисление дисперсии, СКО и коэффициента вариации
print(f"dispers: {mean(squares) - mean(lines) ** 2}")
print(f"sko: {math.sqrt(mean(squares) - mean(lines) ** 2)}") 
print(f"var: {math.sqrt(mean(squares) - mean(lines) ** 2) / mean(lines) * 100}%")


# Вычисление и вывод моды, медианы, минимума, максимума и размаха
print(f"moda: {max(freq.items(), key=lambda x: x[1])})")
print(f"mediana: {sorted(lines)[len(lines) // 2]}")
print(f"min: {min(lines)}")
print(f"max: {max(lines)}")
print(f"razmah: {max(lines) - min(lines)}")

# Вычисление асимметрии и эксцесса
ass = list(sorted(lines))
print("ассиметрия: " + str(sum(map(lambda x: (x - mean(lines)) ** 3, ass)) / len(lines) / math.sqrt(mean(squares) - mean(lines) ** 2) ** 3))
print("эксцесс: " + str(sum(map(lambda x: (x - mean(lines)) ** 4, ass)) / len(lines) / math.sqrt(mean(squares) - mean(lines) ** 2) ** 4 - 3))

# Вычисление и вывод процентов для правила трёх сигм
m = mean(lines)
sko = math.sqrt(mean(squares) - mean(lines) ** 2)

# Процент данных, попадающих в 1, 2 и 3 СКО от среднего значения
perc_68 = sum(1 for x in lines if m - sko < x < m + sko) / len(lines) * 100
perc_95 = sum(1 for x in lines if m - 2 *  sko < x < m + 2 * sko) / len(lines) * 100
perc_99 = sum(1 for x in lines if m - 3 *  sko < x < m + 3 * sko) / len(lines) * 100

# Вывод процентов 68%, 95%, 99% по правилу трёх сигм
print(perc_68, perc_95, perc_99)


# Построение кумулятивной частотной кривой (CDF)
ys = [0]
for k, v in sorted(freq.items()):
    ys.append(ys[-1] + v / len(lines))

plt.plot([0] + xs, ys)
plt.show()
