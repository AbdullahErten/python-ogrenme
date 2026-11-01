araclar = [ {"marka": "BMW", "kilometre": 10000}, {"marka": "Toyota", "kilometre": 15000} ]

araclar.append({"marka": "Mercedes", "kilometre": 20000})
araclar.append({"marka": "Audi", "kilometre": 0})

def bakim_gerekli_mi(kilometre):
    return kilometre % 10000 == 0 and kilometre != 0

for arac in araclar:
    if bakim_gerekli_mi(arac["kilometre"]):
        print(arac["marka"])
    

