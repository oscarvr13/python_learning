name  = input("Cual es tu nombre?: ")
sells = input("How much is your sells?: ")

percentage_sell = 0.13

total_comision = round(float(sells) * percentage_sell, 2)

print(f"Seller: {name} and comission is ${total_comision}")