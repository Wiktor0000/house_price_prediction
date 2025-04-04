import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt


#Wczytywanie danych
housing= pd.read_csv(r"C:\Users\wmusi\OneDrive\Pulpit\house_price_iran\house_price.csv")

#Info
print(housing.info())
print(housing.describe())

#Korelacja
corr=housing.select_dtypes(include="number").corr()
print(corr["Price(USD)"].sort_values(ascending=False))

#Przekształcanie danych, zmiana nazw kolumn
housing.columns= ["area", "room", "parking", "warehouse", "elevator", "price_usd"]
for column in ["parking", "warehouse", "elevator",]:
    housing[column]=housing[column].astype(int)
housing["area"] = pd.to_numeric(housing["area"], errors="coerce")

#Korelacja
corr=housing.select_dtypes(include="number").corr()
print(corr["price_usd"].sort_values(ascending=False))
print(housing.info())

#Rysowanie wykresów
fig, axes= plt.subplots(2, 1,figsize=(12,6))
axes[0].scatter(x=housing["room"], y=housing["price_usd"],
                color="lightcoral", alpha=0.2,  edgecolor="k")
axes[0].set_xlabel("Liczba pokoi")
axes[0].set_ylabel("Cena (USD)")
axes[0].set_title("Wykres rozrzutu dla Price vs Room")
axes[0].grid(True)

axes[1].scatter(x=housing["area"], y=housing["price_usd"],
                color="lightcoral", alpha=0.2, edgecolor="k")
axes[1].set_xlabel("Powierzchnia")
axes[1].set_ylabel("Cena (USD)")
axes[1].set_title("Wykres rozrzutu dla Price vs Area")
axes[1].grid(True)
plt.tight_layout()
plt.show()

#2
parking_counts=housing["parking"].value_counts()
fig, axes=plt.subplots(1, 2, figsize=(12,6))
axes[0].bar(["Brak parkingu", "Jest parking"],
            [parking_counts[0], parking_counts[1]],
            color=["rosybrown", "sienna"],
            edgecolor="black")
axes[0].set_xlabel("Parking")
axes[0].set_ylabel("Liczba")

axes[1].pie(parking_counts,
            labels=["Brak parkingu", "Jest parking"],
            colors=["rosybrown", "sienna"],
            autopct="%1.1f%%",
            explode=[0.03, 0.03],
            wedgeprops={"edgecolor":"black", "linewidth": 1})

fig.suptitle("Wizualizacja 'Zmiennej-Parking' za pomocą wykresu słupkowego i kołowego",
             fontsize=16, fontweight="bold")
plt.tight_layout
plt.show()

#3
elevator_counts=housing["elevator"].value_counts()
fig, axes=plt.subplots(1, 2, figsize=(12, 6))
bars=axes[0].bar(["Brak windy", "Jest winda"],
            [elevator_counts[0], elevator_counts[1]],
            color=["rosybrown", "sienna"],
            edgecolor="black")
axes[0].set_xlabel("Liczba")
axes[0].set_ylabel("Winda")
axes[0].bar_label(bars, fmt='%d', fontsize=12, fontweight='bold')

axes[1].pie(parking_counts,
            labels=["Brak windy", "Jest Winda"],
            colors=["rosybrown", "sienna"],
            autopct="%1.1f%%",
            explode=[0.03, 0.03],
            wedgeprops={"edgecolor":"black", "linewidth": 1})
fig.suptitle("Wizualizacja 'Zmiennej-Elevator' za pomocą wykresu słupkowego i kołowego",
             fontsize=16, fontweight="bold")
plt.tight_layout
plt.show()