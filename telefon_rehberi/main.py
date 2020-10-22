# gerekirse sil # leri

from telefon_rehberi.lib.classAddNewPhoneMenu import AddNewPhoneMenu
# from telefon_rehberi.lib.classEditPhoneMenu import EditPhoneMenu
from telefon_rehberi.lib.classMainMenu import MainMenu
# import telefon_rehberi.res.global_variables as gvars
isim, soyisim, telNo, evNo, email = "", "", 0, 0, ""
# import json


def main():
    mainMenuNames = [
        "Kayıt Ekle", "Kayıt Düzenle", "Kayıt Sil", "Tüm Kayıtları Listele",
        "Ad veya Soyada Göre Bilgileri Getir", "Telefona Göre Bilgileri Getir",
        "Çıkış"
    ]

    # bu ne boka yarıyor
    # ve neden hepsi için ayrı değişken oluşturdun
    # böyle init şeylerinde direkt None verebilirisin
    dumpFile = {
        "İsim: ": isim,
        "Soyisim: ": soyisim,
        "Tel No: ": telNo,
        "Ev No: ": evNo,
        "Email: ": email
    }
    # bunun gibi:
    _ = {
        "İsim: ": None,
        "Soyisim: ": None,
        "Tel No: ": None,
        "Ev No: ": None,
        "Email: ": None
    }
    # değişkeni kullanmamışsın zaten

    mainMenu = MainMenu(mainMenuNames)

    isRunning = True
    while isRunning:
        # sadece bu satır kalmalı
        isRunning = mainMenu.start()
        ############################

        # Burası __redirect_menu fonksiyonunda yapılmalıydı
        # oraya da yazdım
        if isRunning == 1:
            addNewPhoneMenu = AddNewPhoneMenu()
            addNewPhoneMenu.start()

        # TUNAPRO1234
        elif isRunning == 7:
            print("Çıkış yapılıyor...")
            isRunning = False


# if __name__ == "__main__":
#     main()