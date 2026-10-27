def bakim_gerekli_mi(kilometre):
    return kilometre % 10000 == 0


print(bakim_gerekli_mi(10000))
print(bakim_gerekli_mi(12500))