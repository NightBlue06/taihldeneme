sozluk = {"elma": "apple", "kitap": "book", "kalem": "pencil"}

# Sözlüklerin elemanlarına erişme
print(sozluk["elma"])
print(sozluk.get("elma"))
print(sozluk.get("siyah", "yok"))

# Sözlüklere eleman ekleme
sozluk["masa"] = "table"
sozluk["kırmızı"] = "red"
print(sozluk)

# Sözlüklerden eleman sime
del sozluk["masa"]
print(sozluk)

# SÖZLÜK METOTLARI
# keys()
print(sozluk.keys())

# values()
print(sozluk.values())

# items()
print(sozluk.items())

# İç içe sözlükler
ogrenciler = {
    "9/C": {"isim": "Yasuo", "soyad": "Penta kill", "dogum_tarihi": 3131},
    "9/B": {"isim": "Sett", "soyad": "Furry", "dogum_tarihi": 6969, "notlar": [80, 95]}
}
for sinif, ogrenci in ogrenciler.items():
    for key, value in ogrenci.items():
        print(f"Sınıf: {sinif}, {key}: {value}")

print(ogrenciler["9/B"]["notlar"])
