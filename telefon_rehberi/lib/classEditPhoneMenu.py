import json
from json import dump
import telefon_rehberi.res.global_variables as gvars
from telefon_rehberi.lib.classMainMenu import MainMenu, telefonlar
isim, soyisim, telNo, evNo, email = "", "", 0, 0, ""


class EditPhoneMenu(MainMenu):
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
                     len("Telefon Kaydı Düzenleme Menüsüne Hoşgeldiniz!") / 2)
        print(
            "\n" * 3 + " " * offset +
            "Telefon Kaydı Düzenleme Menüsüne Hoşgeldiniz!" + " " * offset,
            "\n" + "#" * len(" " * offset +
                             "Telefon Kaydı Düzenleme Menüsüne Hoşgeldiniz!" +
                             " " * offset))

    def start(self):
        self.print_menu()
        inpList = []
        falseCheck = 3
        index = -1
        check = input(
            "Düzenlemek istediğiniz kaydın telefon numarasını giriniz: ")
        while not falseCheck == 0:
            for i in telefonlar:
                index += 1
                if i['Tel No: '] == check:
                    for i in range(len(self.addPhoneMenuInputs)):
                        inp = input(
                            "Yapmak istediğiniz değişikliği girin, yoksa Enter'a basın",
                            self.addPhoneMenuInputs[i])
                        inpList.append(inp)
                    i = 0
                    for key in self.dumpFile:
                        self.dumpFile[key] = inpList[i]
                        i += 1
                    self.dumpFile = {
                        "İsim: ":
                        i['İsim: '] if inpList[0].capitalize() == '' else
                        inpList[0].capitalize(),
                        ###########################
                        "Soyisim: ":
                        i['Soyisim: '] if inpList[1].capitalize() == '' else
                        inpList[1].capitalize(),
                        ###########################
                        "Tel No: ":
                        i['Tel No: '] if inpList[2] == '' else inpList[2],
                        ###########################
                        "Ev No: ":
                        i['Ev No: '] if inpList[3] == '' else inpList[3],
                        ###########################
                        "Email: ":
                        i['Email: '] if inpList[4] == '' else inpList[4],
                    }
                    telefonlar[index].update(self.dumpFile)
                    self.write_phones(telefonlar)
                    break
            check = input(
                "Telefon numarasını yanlış girdiniz lütfen tekrar deneyin: ")

    def write_phones(obj, path=gvars.jsonFilePath):
        try:
            with open(path, "w+") as file:
                json.dump(obj, file)
        except:
            print("Kayıt Düzenleme Başarısız...")
            return False
        print("Kayıt Başarıyla Düzenlendi!")
        return True