class Ogrenci:
    def __init__(self, isim, soyisim, yil):
        self.ad = isim
        self.soyad = soyisim
        self.dogum_yili = yil
        self.notlar = []

    def not_ekle(self, puan):
        self.notlar.append(puan)

    def not_ortalama(self):
        if not self.notlar:
            return "Lütfen önce not ekleyin"
        ortalama = sum(self.notlar) / len(self.notlar)

        return ortalama

    def tam_ad(self):
        return f"{self.ad} {self.soyad}"