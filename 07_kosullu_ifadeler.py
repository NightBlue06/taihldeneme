# if koşulu
yas = 15  # int(input("Yaşınız: "))
if yas >= 18:
    print(f"Yaşınız {yas} olduğu için; reşitsiniz.")

# else koşulu
else:
    print(f"Yaşınız {yas} olduğu için; reşit değilsiniz.")


# Kullanıcıdan bir sayı alın.
# Sayı 10'dan büyük veya eşitse
#   "Sayı 10'a eşit veya büyük",
# değilse
#   "Sayı 10'dan küçük" yazdırın.
sayi = 7  # float(input("Bir sayı giriniz: "))
if sayi >= 10:
    print(f"{sayi}, 10'dan büyük veya eşittir.")
else:
    print(f"{sayi}, 10'dan küçüktür.")

# elif koşulu
""" 
 Kullanıcıdan bir sayı alın.
 Sayı 10'dan büyükse.
   "Sayı 10'dan büyüktür.",
 Sayı 10'a eşitse
   "Sayı 10'a eşittir."
 değilse
   "Sayı 10'dan küçük" yazdırın.
"""
sayi = 15  # int(input("Bir sayı giriniz: "))
if sayi > 10:
    print(f"{sayi}, 10'dan büyüktür.")
elif sayi == 10:
    print(f"{sayi}, 10'a eşittir.")
else:
    print(f"{sayi}, 10'dan küçüktür.")

# iç içe koşullu ifadeler
kullanici_adi = "NightBlue06"
sifre = "123456"
if kullanici_adi == "NightBlue06":
    print("Kullanıcı adı doğru")

    if sifre == "123456":
        print("Şifre doğru")
        print("Giriş yaptınız.")

# yukarıdaki işlemi mantıksal operatörler kullanarak yapalım.
if kullanici_adi == "NightBlue06" and sifre == "123456":
    print("Kullanıcı adı doğru")
    print("Şifre doğru")
    print("Giriş yaptınız.")

# Tek satırlık koşullu ifadeler (ternary operators)
x = 10
y = 20
if x > y:
    maksimum = x
else:
    maksimum = y

# Tek satırlık örnek
maksimum = x if x > y else y  # PHP: maksimum = x > y ? x : y

print(maksimum)
