prices = [97, 56.78, 89.76, 32.45, 12.78, 83.84, 26.89, 67.87, 34.68, 23]
new_list = []
for price in prices:
    roubles = int(price)
    kop = round((price - roubles) * 100)
    new_list.append(f"{roubles} руб {kop:02} коп")
print(", ".join(new_list))
id1 = id(prices)
prices.sort()
print(prices)
print(id(prices) == id1)
my_list = sorted(prices, reverse=True)
print(sorted(my_list[:5]))