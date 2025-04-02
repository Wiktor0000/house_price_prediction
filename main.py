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
plt.show()
print(housing.head())