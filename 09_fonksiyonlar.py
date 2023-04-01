"""
Fonksiyon tanımlarken Python içindeki özel ifadeleri
ve fonksiyon isimlerini kullanmalıyız.

Fonksiyon söz dizimi:

def fonksiyon_adi(parametre1, parametre2):
    # işlemler yapılır
    return deger
"""


# Toplama işlemi yapan bir fonksiyon yazalım
def topla(a, b):
    sonuc = a + b
    return sonuc


toplam = topla(7, 9)
print(toplam)
print(topla(4, 6))


# Faktoriyel hesaplayan bir fonksiyon yazalım
def faktoriyel(n):
    if n == 0:
        return 1

    return n * faktoriyel(n-1)


f = faktoriyel(5)
print(f)

def toplama(*args):
    # *args: (4, 7, 10, 15)
    toplam = 0
    for sayi in args:
        toplam += 1

    return toplam

print(toplama(4, 7, 10, 15))
print(toplama(5, 4))
print(toplama(1, 2, 3, 4, 5, 6, 7, 8, 9))
print(toplama())
def ogrenci_bilgileri(**kwargs):
     # **kwargs: {"ad": "Eren", "soyad": "Özdal", "yas": 15}
    for anahtar, deger in kwargs.items():
        print(f"{anahtar}: {deger}")


ogrenci_bilgileri(ad="Yasin", soyad="Ömeroğlu", yas=15, dersler=["Türkçe", "Matematik"])

# Lambda Fonksiyonları

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
kareler = list(map(lambda x: x ** 2, liste))
print(kareler)

liste1 = [4, 6]
liste2 = [8, 12]
toplamlar = list(map(lambda x, y: x + y, liste1, liste2))
print(toplamlar)

# İç içe fonksiyonlar
def dort_islem(sayi1, sayi2, islem="toplama"):
     def toplama(x, y):
         return x + y

     def cikarma(x, y):
         return x - y

     def carpma(x, y):
         return x * y

     def bolme(x, y):
         return x / y

     if islem == "toplama":
         return toplama(sayi1, sayi2)
     elif islem == "çıkarma":
         return cikarma(sayi1, sayi2)
     elif islem == "çarpma":
         return carpma(sayi1, sayi2)
     elif islem == "bölme":
         return bolme(sayi1, sayi2)
     else:
         return "Yanlış işlem seçtiniz"

print("Toplama:", dort_islem(2, 3))
print("Çıkarma:", dort_islem(2, 3))
print("Çarpma:", dort_islem(2, 3))
print("Bölme:", dort_islem(2, 3))
print("Hata:", dort_islem(2, 3, "kare alma"))
