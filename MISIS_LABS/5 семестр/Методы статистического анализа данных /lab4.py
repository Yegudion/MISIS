from collections import defaultdict
import scipy.stats as stats

alpha = 0.05 # Уровень значимости

lines = open("Москва_2021.txt").readlines()
lines = list(map(int, lines))

freq = defaultdict(int)

def mean(arr: list[int]):
    return sum(arr) / len(arr)


for num in lines:
    freq[num] += 1

n = len(freq)
meanx = sum(freq.keys())/n
meany = sum(freq.values())/n
sigma_x = (sum(i**2 for i in freq.keys())/n - meanx**2)**(1/2)
sigma_y = (sum(i**2 for i in freq.values())/n - meany**2)**(1/2)
meanxy = sum(i*j for i,j in freq.items())/n

print("Среднее значение x:", meanx)
print("Среднее значение y:", meany)
print("Стандартное отклонение x:", sigma_x)
print("Стандартное отклонение y:", sigma_y)
print("Среднее значение произведения x и y:",meanxy)
kkxy = (meanxy - meanx*meany)/(sigma_x*sigma_y)
print('Коэффициент корреляции x и y равен:', kkxy)
tnabl = kkxy*(n-2)**(1/2)/(1-kkxy**2)**(1/2)
print("Наблюдаемое значение:",tnabl)




tcritical = stats.t.ppf(1 - alpha / 2, df=n - 2)

print(f"Критическое значение для двустороннего критерия: {tcritical:.4f}")
if abs(tnabl)<tcritical:
  print("Гипотеза принимается. Величины X и Y независимы")
else:
  print("Нулевая гипотеза отвергается. Выборочный коэффициент корреляции 𝑟𝑥𝑦 значимо отличается от нуля. Следовательно величины X и Y коррелированы. ")


# задание 3
import matplotlib.pyplot as plt
plt.figure(figsize=(15,6))
plt.scatter(freq.keys(), freq.values())
plt.grid(visible=True)

plt.show()
intervals={}
intervals_av={}
intervals_disp={}
for i in range (14,73,9):
  intervals[str(i)+'-'+str(i+9)]=0
  intervals_av[str(i)+'-'+str(i+9)]=0
  intervals_disp[str(i)+'-'+str(i+9)]=0

for i in freq:
  for j in intervals:
    l, r = (int(number) for number in j.split('-'))
    if i>=l and i<r:
      intervals[j]+=freq[i]
      intervals_av[j]+=i*freq[i]
      intervals_disp[j]+=i**2*freq[i]

for i in intervals:
  intervals_av[i]/=intervals[i]
  intervals_disp[i]/=intervals[i]

for i in intervals_disp:
  intervals_disp[i]=intervals_disp[i]-intervals_av[i]**2

disp_vngr = 0
for i in intervals_disp:
  disp_vngr +=intervals_disp[i]*intervals[i]/sum(freq.values())

print("Внутригрупповая дисперсия",disp_vngr)

disp_mgr = 0
disp_mgr = 0
average = sum(int(i) for i in lines)/len(lines)
disp_mgr = 0


for i in intervals_av:
  disp_mgr += ((intervals_av[i]-average)**2)*intervals[i]/len(lines)

print("Межгрупповая дисперсия",disp_mgr)

disp_ob = disp_vngr+disp_mgr
print("Общая дисперсия",disp_ob)

kor_otn = (disp_mgr/disp_ob)**(1/2)
print("Корреляционное отношение:",kor_otn)
