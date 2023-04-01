liste = [1, 2, True, "Yasin", (1, 2, 3), {"a": 12, "b": 7 }]

# Listenin elemanlarına erişme
print(liste[0])
print(liste[-1])

# Listenin elemanlarını değiştirme
liste[2] = "elma"
print(liste)

# LİSTE METOTLARI
# append()
meyveler = ["elma", "armut", "çilek"]
meyveler.append("erik")
print(meyveler)

# insert()
meyveler.insert(2, "karpuz")
print(meyveler)

# remove()
meyveler.append("erik")
print(meyveler)
meyveler.remove("erik")
print(meyveler)
# meyveler.remove("kavun") liste içinde olmadığı için hata verdi
meyveler.remove("elma")
print(meyveler)

# pop()
silinen = meyveler.pop()
print(meyveler)
print(silinen)
silinen = meyveler.pop(1)
print(meyveler)
print(silinen)

# sort()
sayilar = [89, 42, 70, 12, 53, 89]
isimler = ["Zeynep", "Eren", "Fatma", "Muhammed", "Kerem"]
sayilar.sort()
print(sayilar)
sayilar.sort(reverse=True)
print(sayilar)
isimler.sort()
print(isimler)
isimler.sort(reverse=True)
print(isimler)

# count()
isim = "Yasin Ömeroğlu"
karakterler = [x for x in isim.lower()]
print(karakterler)
print(karakterler.count("y"))

# İç içe geçmiş listeler (matris)
ogrenciler = [
    ["Yasuo", 70, 64, 85],
    ["Sett", 90, 75, 85]
]
print(f"{ogrenciler[0][0]} isimli öğrencinin notları: {ogrenciler[0][1:]}")
