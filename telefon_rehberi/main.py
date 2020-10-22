import telefon_rehberi.res.global_variables as gvars
import json
from telefon_rehberi.lib.classMainMenu import MainMenu
from telefon_rehberi.lib.classEditPhoneMenu import EditPhoneMenu
from telefon_rehberi.lib.classAddNewPhoneMenu import AddNewPhoneMenu
isim, soyisim, telNo, evNo, email = "", "", 0, 0, ""


def main():
    mainMenuNames = [
        "Kayıt Ekle", "Kayıt Düzenle", "Kayıt Sil", "Tüm Kayıtları Listele",
        "Ad veya Soyada Göre Bilgileri Getir", "Telefona Göre Bilgileri Getir",
        "Çıkış"
    ]
    dumpFile = {
        "İsim: ": isim,
        "Soyisim: ": soyisim,
        "Tel No: ": telNo,
        "Ev No: ": evNo,
        "Email: ": email
    }
    mainMenu = MainMenu(mainMenuNames)

    isRunning = True
    while isRunning:
        isRunning = mainMenu.start()
        if isRunning == 1:
            addNewPhoneMenu = AddNewPhoneMenu()
            addNewPhoneMenu.start()
        elif isRunning == 7:
            print("Çıkış yapılıyor...")
            isRunning = False


if __name__ == "__main__":
    main()