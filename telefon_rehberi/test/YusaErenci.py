import json
import os

os.system('cls')


def jsongetir():
    with open("telefonlar.json", "r", encoding="utf-8") as f:
        telveriler = json.load(f)
    return telveriler


def jsonguncelle(telveriler):
    with open("telefonlar.json", "w", encoding="utf-8") as f:
        json.dump(telveriler, f, indent=4, ensure_ascii=False)


def menuolustur():
    print("""
                  TELEFON DEFTERİ
              =======================================
               1- Kayıt Ekle
               2- Kayıt Düzenle 
               3- Kayıt Sil
               4- Tüm Kayıtları Listele
               5- Ad veya Soyada Göre Bilgileri Getir
               6- Telefona Göre Bilgileri Getir
               7- Çıkış
              =======================================
  """)
    secim = input("Lütfen Yapmak İstediğiniz İşlem İçin Kodu Giriniz: ")
    return secim


def kayitekle(tellistveri):
    ad = input("Kaydetmek istediğiniz kişinin adını giriniz: ")
    soyad = input("Kaydetmek istediğiniz kişinin soyadını giriniz: ")
    ceptel = input("Kaydetmek istediğiniz kişinin cep telefonunu giriniz: ")
    evtel = input("Kaydetmek istediğiniz kişinin ev telefonunu giriniz: ")
    il = input("Kaydetmek istediğiniz kişinin yaşadığı ili giriniz: ")
    email = input("Kaydetmek istediğiniz kişinin email adresini giriniz: ")
    kayit = {
        "ad": ad.capitalize(),
        "soyad": soyad.capitalize(),
        "ceptel": ceptel,
        "evtel": evtel,
        "il": il.capitalize(),
        "email": email,
    }
    telefonverileri.append(kayit)
    jsonguncelle(telefonverileri)
    print(ad, soyad, "rehberinize kaydedilmiştir.")


def kayitduzenle(tellistveri):
    duzenleme = input("Düzenlemek istediğiniz kaydın cep telefonunu giriniz: ")
    indeks = -1
    for i in tellistveri:
        indeks += 1
        if i['ceptel'] == duzenleme:
            ad = input(
                "Kaydın adında yapmak istediğiniz değişikliği giriniz, yoksa enter'a basıp geçiniz: "
            )
            soyad = input(
                "Kaydın soyadında yapmak istediğiniz değişikliği giriniz, yoksa enter'a basıp geçiniz: "
            )
            ceptel = input(
                "Kaydın cep no'sunda yapmak istediğiniz değişikliği giriniz, yoksa enter'a basıp geçiniz: "
            )
            evtel = input(
                "Kaydın ev no'sunda yapmak istediğiniz değişikliği giriniz, yoksa enter'a basıp geçiniz: "
            )
            il = input(
                "Kaydın yaşadğı il bilgisinde yapacağınız değişikliği giriniz, yoksa enter'a basıp geçiniz: "
            )
            email = input(
                "Kaydın email adresinde yapmak istediğiniz değişikliği giriniz, yoksa enter'a basıp geçiniz: "
            )
            kayit = {
                "ad":
                i['ad'] if ad.capitalize() == '' else ad.capitalize(),
                "soyad":
                i['soyad'] if soyad.capitalize() == '' else soyad.capitalize(),
                "ceptel":
                i['ceptel'] if ceptel == '' else ceptel,
                "evtel":
                i['evtel'] if evtel == '' else evtel,
                "il":
                i['il'] if il.capitalize() == '' else il.capitalize(),
                "email":
                i['email'] if email == '' else email,
            }
            telefonverileri[indeks].update(kayit)
            jsonguncelle(telefonverileri)
            print(i['ad'], i['soyad'], "kaydı düzenlenmiştir.")
            break


def kayitsil(tellistveri):
    kayit = input("Silmek istediğiniz kaydın cep telefonunu giriniz: ")
    indeks = -1
    for i in tellistveri:
        indeks += 1
        if i['ceptel'] == kayit:
            tellistveri.pop(indeks)
            jsonguncelle(telefonverileri)
            print(i['ad'], i['soyad'], "rehberinizden silinmiştir")
            break


def tlistele(tellistveri):
    for i in tellistveri:
        print("Adı Soyadı:", (i['ad'] + " " + i['soyad']).ljust(17),
              "Cep Telefonu: ", i['ceptel'].ljust(15), "Ev Telefonu: ",
              i['evtel'].ljust(15), "Yaşadığı İl: ", i['il'].ljust(12),
              "Email adresi: ", i['email'])


def adsadgorebul(tellistveri):
    ad, soyad = input("Aradığınız kaydın adını giriniz: "), input(
        "Aradığınız kaydın soyadını giriniz: ")
    print("girdiğiniz ad ve soyada uyan kayıtlarınız bunlardır: ")
    for i in tellistveri:
        if i['ad'] == ad.capitalize() or i['soyad'] == soyad.capitalize():
            print(i)


def telgorebul(tellistveri):
    telegorearama, evegorearama = input(
        "Aradığınız kaydın cep telefonunu giriniz: "), input(
            "aradığınız kaydın ev telefonunu giriniz: ")
    print("girdiğiniz numaralara uyan kayıtlarınız bunlardır: ")
    for i in tellistveri:
        if i['ceptel'] == telegorearama or i['evtel'] == evegorearama:
            print(i)


def main():
    # Main fonksiyon buradan başlıyor.
    # Fonksiyon tanımlamalarını, Main fonksiyonunun üzerinde tanımlayınız.
    telefonverileri = jsongetir(
    )  # telefonlar.json dosyasındaki verileri getir.

    giris = 'e'

    while True:
        while giris == 'e':
            secim = menuolustur()  # menüden seçilen kodu al
            if secim == "1":
                kayitekle(telefonverileri)
            elif secim == "2":
                kayitduzenle(telefonverileri)
            elif secim == "3":
                kayitsil(telefonverileri)
            elif secim == "4":
                tlistele(telefonverileri)
            elif secim == "5":
                adsadgorebul(telefonverileri)
            elif secim == "6":
                telgorebul(telefonverileri)
            elif secim == "7":
                break
            else:
                print("1-7 arasında bir değer seçmelisin!")
        giris = input("Tekrar giriş yapmak istermisiniz(e/h): ")
        if giris == 'h':
            break
        elif giris != 'e':
            secim = ''
            print(
                "Giriş yada Çıkış için 'e' veya 'h' harflerinden birini seçmelisin!"
            )


if __name__ == "__main__":
    main()