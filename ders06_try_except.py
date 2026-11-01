araclar = [{"marka": "BMW"}]


def arac_getir(index):
    try:
        return araclar[index]["marka"]
    except IndexError:
        return None


print(arac_getir(0))
print(arac_getir(1))
print(arac_getir(10))

sonuc = arac_getir(10)
if sonuc is None:
    print("Arac bulunamadi")