import telefon_rehberi.res.global_variables as gvars
import json
from telefon_rehberi.lib.classes import MainMenu, EditPhoneMenu, AddNewPhoneMenu
# from telefon_rehberi.lib.classMainMenu import MainMenu
# from telefon_rehberi.lib.classEditPhoneMenu import EditPhoneMenu
# from telefon_rehberi.lib.classAddNewPhoneMenu import AddNewPhoneMenu
# classes.funcReturnClasses()


def read_phones(path=gvars.jsonFilePath):
    with open(path) as file:
        read = json.load(file)
    return read


def write_phones(obj, path=gvars.jsonFilePath):
    try:
        with open(path, "w+") as file:
            json.dump(obj, file)
    except:
        return False
    return True


def main():
    mainMenuNames = [
        "Kayıt Ekle", "Kayıt Düzenle", "Kayıt Sil", "Tüm Kayıtları Listele",
        "Ad veya Soyada Göre Bilgileri Getir", "Telefona Göre Bilgileri Getir",
        "Çıkış"
    ]

    addPhoneMenuInputs = {
        "İsim: ": isim,
        "Soyisim: ": soyisim,
        "Tel No: ": telNo,
        "Ev No: ": evNo,
        "Email: ": email
    }
    isRunning = True
    while isRunning:
        isRunning = mainMenu.start()


if __name__ == "__main__":
    main()