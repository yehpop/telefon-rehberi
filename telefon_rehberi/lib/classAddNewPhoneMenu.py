import json
import telefon_rehberi.res.global_variables as gvars
from telefon_rehberi.lib.classMainMenu import MainMenu, telefonlar
isim, soyisim, telNo, evNo, email = "", "", 0, 0, ""


class AddNewPhoneMenu(MainMenu):
    def __init__(self):
        self.addPhoneMenuInputs = [
            "İsim: ", "Soyisim: ", "Tel No: ", "Ev No: ", "Email: "
        ]
        self.dumpFile = {
            "İsim: ": isim,
            "Soyisim: ": soyisim,
            "Tel No: ": telNo,
            "Ev No: ": evNo,
            "Email: ": email
        }

    def print_menu(self):
        maxLenA = 0
        for menu in self.addPhoneMenuInputs:
            if len(menu) > maxLenA:
                maxLenA = len(menu)
        offset = int(maxLenA / 2 -
                     len("Yeni Telefon Kaydı Ekleme Menüsüne Hoşgeldiniz!") /
                     2)
        print(
            "\n" * 3 + " " * offset +
            "Yeni Telefon Kaydı Ekleme Menüsüne Hoşgeldiniz!" + " " * offset,
            "\n" +
            "#" * len(" " * offset +
                      "Yeni Telefon Kaydı Ekleme Menüsüne Hoşgeldiniz!" +
                      " " * offset))

    # def redirect_input(self, inp: int):
    #   print(self.addPhoneMenuInputs[inp])

    def start(self):
        self.print_menu()
        inpList = []
        for i in range(len(self.addPhoneMenuInputs)):
            inp = input(self.addPhoneMenuInputs[i])
            inpList.append(inp)
        i = 0
        for key in self.dumpFile:
            self.dumpFile[key] = inpList[i]
            i += 1
        print(self.dumpFile)
        telefonlar.append(self.dumpFile)
        self.write_phones(telefonlar)

    def write_phones(obj, path=gvars.jsonFilePath):
        try:
            with open(path, "w+") as file:
                json.dump(obj, file)
        except:
            print("Kayıt Eklenemedi...")
            return False
        print("Kayıt Eklenmiştir!")
        return True
