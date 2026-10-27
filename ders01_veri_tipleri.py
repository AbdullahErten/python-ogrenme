araba = {
    "marka": "BMW",
    "model_yili": 2026,
    "kilometre": 10000,
    "bakimda_mi": False,
    "son_bakimlar": ["2026.08.19", "2026.10.14", "2026.12.17"],
}

print(araba["marka"])

yeni_kilometre = araba["kilometre"] + 500
print(yeni_kilometre)

uzunluk = len(araba["son_bakimlar"])
print(uzunluk)