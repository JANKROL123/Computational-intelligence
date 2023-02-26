import math

import pandas as pd
from matplotlib import pyplot as plt

# a
miasta_pd = pd.read_csv("miasta.csv")
miasta = miasta_pd.values
# b
data = [[2010,460,555,405]]
df = pd.DataFrame(data)
df.to_csv("miasta.csv", mode='a', index=False, header=False)
# c d
data_c = pd.read_csv("miasta.csv")
plt.plot(data_c.Rok, data_c.Gdansk, color = "red", marker = "o", label = "Gdansk")
plt.plot(data_c.Rok, data_c.Poznan, color = "blue", marker = "o", label = "Poznan")
plt.plot(data_c.Rok, data_c.Szczecin, color = "green", marker = "o", label = "Szczecin")
plt.title("Liczba ludnosci w miastach Polski")
plt.xlabel("Rok")
plt.ylabel("Ludnosc")
plt.legend()
plt.draw()
plt.show()
# e

def mean(tab):
    total = 0
    for i in tab:
        total += i 
    result = total / len(tab)
    return result
def sd(tab):
    my_mean = mean(tab)
    sum_var = 0
    for i in tab:
        sum_var += (i - my_mean)**2
    var = sum_var / len(tab)
    sd = math.sqrt(var)
    return sd

gdansk = []
poznan = []
szczecin = []
for i in miasta:
    gdansk.append(i[1])
    poznan.append(i[2])
    szczecin.append(i[3])
gdansk_standaryzacja = []
poznan_standaryzacja = []
szczecin_standaryzacja = []
mean_gdansk = mean(gdansk)
mean_poznan = mean(poznan)
mean_szczecin = mean(szczecin)
sd_gdansk = sd(gdansk)
sd_poznan = sd(poznan)
sd_szczecin = sd(szczecin)
for i in gdansk:
    z = (i - mean_gdansk) / sd_gdansk
    gdansk_standaryzacja.append(z)
for i in poznan:
    z = (i - mean_poznan) / sd_poznan
    poznan_standaryzacja.append(z)
for i in szczecin:
    z = (i - mean_szczecin) / sd_szczecin
    szczecin_standaryzacja.append(z)
print("Standaryzacja 1")
print(f"Gdańsk -> średnia: {mean(gdansk_standaryzacja)}, odchylenie: {sd(gdansk_standaryzacja)}")
print(f"Gdańsk -> średnia: {mean(gdansk_standaryzacja)}, odchylenie: {sd(gdansk_standaryzacja)}")
print(f"Gdańsk -> średnia: {mean(gdansk_standaryzacja)}, odchylenie: {sd(gdansk_standaryzacja)}")
# f
gdansk_standaryzacja2 = []
poznan_standaryzacja2 = []
szczecin_standaryzacja2 = []
min_gdansk = min(gdansk)
min_poznan = min(poznan)
min_szczecin = min(szczecin)
max_gdansk = max(gdansk)
max_poznan = max(poznan)
max_szczecin = max(szczecin)
for i in gdansk:
    z = (i - min_gdansk) / (max_gdansk - min_gdansk)
    gdansk_standaryzacja2.append(z)
for i in poznan:
    z = (i - min_poznan) / (max_poznan - min_poznan)
    poznan_standaryzacja2.append(z)
for i in szczecin:
    z = (i - min_szczecin) / (max_szczecin - min_szczecin)
    szczecin_standaryzacja2.append(z)
print("Standaryzacja 2")
print(f"Gdansk -> min: {min(gdansk_standaryzacja2)}, max: {max(gdansk_standaryzacja2)}")
print(f"Poznan -> min: {min(poznan_standaryzacja2)}, max: {max(poznan_standaryzacja2)}")
print(f"Szczecin -> min: {min(szczecin_standaryzacja2)}, max: {max(szczecin_standaryzacja2)}")