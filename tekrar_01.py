futbolcu = {"isim": "Lionel Messi", "gol": 0, "aktif": True, "son_maclar": ["2026.08.19", "2026.10.14", "2026.12.17"]}
print(futbolcu["gol"] + 3)
def tehlikeli_mi(gol):
    return gol % 10 == 0 and gol != 0

print(tehlikeli_mi(futbolcu["gol"]))   