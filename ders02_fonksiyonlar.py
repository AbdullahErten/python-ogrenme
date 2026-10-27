def bakim_gerekli_mi(kilometre):
    return kilometre % 10000 == 0 and kilometre != 0

print(bakim_gerekli_mi(0))        # false
print(bakim_gerekli_mi(10000))    # true
print(bakim_gerekli_mi(12500))    # false