def bakim_durumu(kilometre):
    
    if kilometre % 10000 == 0 and kilometre != 0:
        return "Bakım gerekli."
    else:
        return "Bakım gerekli değil."

kilometreler = [0, 5000, 10000, 15000, 20000]

for km in kilometreler:
    print(f"{km} km: {bakim_durumu(km)}")

for oyuncu_gol in [3,10,25]:
    print(f"{oyuncu_gol} gol")

