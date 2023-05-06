import sqlite3

# Veri tabanına bağlanalım
baglanti = sqlite3.connect("ornek.db")

# Veritabanında işlem yapılmasını sağlayan imleç nesnesi
imlec = baglanti.cursor()

# Veritabanı tablosu oluşturalım
imlec.execute("CREATE TABLE IF NOT EXISTS ogrenciler (ad text, soyad text, dogum_tarihi integer)")

# Veritabanına veri ekleyelim
imlec.execute("INSERT INTO ogrenciler VALUES ('Sett', 'Yumrukoğlu', '2000')")

# İşlemleri kaydedelim
baglanti.commit()

# Bağlantıyı kapatalım
baglanti.close()
