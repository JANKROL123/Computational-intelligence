import pandas as pd
from matplotlib import pyplot as plt
import math

miasta = pd.read_csv("miasta.csv").values

data = [[2010,460,555,405]]
df = pd.DataFrame(data)
df.to_csv("miasta.csv", mode='a', index=False, header=False)
print("Added")

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

data_c = pd.read_csv("miasta.csv")
plt.plot(data_c.Rok, data_c.Gdansk, color = "red", marker = "o", label = "Gdansk")
plt.plot(data_c.Rok, data_c.Poznan, color = "blue", marker = "o", label = "Poznan")
plt.plot(data_c.Rok, data_c.Szczecin, color = "green", marker = "o", label = "Szczecin")
plt.title("Liczba ludnosci w miastach Polski")
plt.xlabel("Rok")
plt.ylabel("Ludnosc")
plt.legend()
plt.show()

