import json
import telefon_rehberi.res.global_variables as gvars
from telefon_rehberi.lib.classMainMenu import MainMenu
isim, soyisim, telNo, evNo, email = "", "", 0, 0, ""


class AddNewPhoneMenu(MainMenu):
    def __init__(self):
        self.addPhoneMenuInputs = {
            "İsim: ": isim,
            "Soyisim: ": soyisim,
            "Tel No: ": telNo,
            "Ev No: ": evNo,
            "Email: ": email
        }

    def addPhone(self, obj):
        self.write_phones(obj)

    def print_menu(self):
        maxLenA = 0
        for menu in self.addPhoneMenuInputs:
            if len(menu) > maxLenA:
                maxLenA = len(menu)
        offset = maxLenA / 2 - len("Telefon Kaydı Ekleme Menüsü") / 2
        print(" " * offset, "Telefon Kaydı Ekleme Menüsü", " " * offset)

    def start(self):
        self.print_menu()


def write_phones(obj, path=gvars.jsonFilePath):
    try:
        with open(path, "w+") as file:
            json.dump(obj, file)
    except:
        return False
    return True
