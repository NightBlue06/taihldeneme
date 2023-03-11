x = 5
y = "Merhaba, Yasin X_X"
z = True

# VERİ TİPLERİ
# 1. Tam sayılar (integer)
x = 15
y = -15
z = 0

# 2.  Ondalıklı sayılar (floats)

x = 3.14
y = -2.25
z = 1.0

# 3. Metin (string)
selam = "Neden ölmedin"
ad = "Yasin"
mesaj = selam + " " + ad
print(mesaj)

# 4. Boolean (True veya False)
x = True
y = False

a = 7
b = 3
print(a > b)  # True
print(a == b)  # False

# 5. Listeler (list)
meyveler = ["elma", "armut", "portakal", "karpuz"]
print(meyveler)
print(len(meyveler))
print(meyveler[0])  # ilk eleman
print(meyveler[3])  # çalışır ama her zaman bilinmez
print(meyveler[len(meyveler) - 1])  # son eleman uzun yoldan ulaştık
print(meyveler[-1])  # son eleman
meyveler[1] = "kivi"
print(meyveler)

# 6. Demetler (tuple)
sayilar = (1, 2, 3)
print(sayilar)
print(len(sayilar))
print(sayilar[0])  # ilk eleman
print(sayilar[-1])
# sayilar[1] = 4 -> tuple içindeki elemanlar değişmez
print(sayilar)

# 7. Sözlükler (dictionary -> dict)
# anahtar = değer
sozluk = {
    "marka": "Apple",
    "model": "Iphone SE 2020",
    "yıl": "2021",
}
print(sozluk)
print(sozluk["marka"])
print(sozluk.get("marka"))
print(sozluk.get("fiyat", 0.0))
sozluk["fiyat"] = 15000.0
print(sozluk)
print(sozluk.get("fiyat", 0.0))

# 8. Kümeler (set)
kume = {1, 2, 3, 4, 5}
print(kume)
kume.add(6)
print(kume)
kume.add(6)
print(kume)
kume.add("Yasin")
print(kume)
kume.remove("Yasin")
print(kume)
kume.update([6, 7, "Yasin", "Seraphine", "Yasin"])
print(kume)

# VERİ TİPİ DÖNÜŞÜMLERİ
sayi1 = "6"  # input("1. sayıyı yazın: ")
sayi2 = "7"  # input("2. sayıyı yazın: ")
toplam = sayi1 + sayi2  # string değerlerini birleştirdi
print(type(sayi1), type(sayi2))
sayi1 = int(sayi1)
sayi2 = int(sayi2)
print(type(sayi1), type(sayi2))
print(sayi1 + sayi2)

x = 1
y = 1.8
liste = ["Türkçe", "Matematik", "Geometri", "Türkçe"]
print(float(x))
print(int(y))
print(x + y)
print(bool(x))  # True
print(bool(y))  # True
print(bool(0))  # False
print(bool(0.8))  # True
print(bool(-1))  # True
print(bool(int(0.8)))  # False
print(int(True))
print(int(False))
print(type(str(x)))
print(type(str(y)))
print(tuple(liste))
print(set(liste))
