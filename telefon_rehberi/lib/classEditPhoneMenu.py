# from telefon_rehberi.lib.classMainMenu import MainMenu

# from telefon_rehberi.lib.classMainMenu import MainMenu, telefonlar
import telefon_rehberi.res.global_variables as gvars
isim, soyisim, telNo, evNo, email = "", "", 0, 0, ""

# from json import dump
# import json


# class EditPhoneMenu(MainMenu):
class EditPhoneMenu:
    def __init__(self):
        self.addPhoneMenuInputs = [
            "İsim: ", "Soyisim: ", "Tel No: ", "Ev No: ", "Email: "
        ]

        # Bunları None yap
        # ya da sadece keylerin tutulduğu arraya dönüştür
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

        # yapf: disable
        check = input("Düzenlemek istediğiniz kaydın telefon numarasını giriniz: ")
        # yapf: enable

        # index kullanman gerekmiyor enumerate var
        index = -1
        inpList = []
        falseCheck = 3
        while not falseCheck == 0:
            # index tutarken i yerine j dersen ya da daha uzun isim kullanırsan daha iyi olur

            # for index, i in enumerate(gvars.telefonlar):
            for i in gvars.telefonlar:
                index += 1
                if i['Tel No: '] == check:
                    for i in range(len(self.addPhoneMenuInputs)):
                        inp = input(
                            "Yapmak istediğiniz değişikliği girin, yoksa Enter'a basın",
                            self.addPhoneMenuInputs[i])
                        inpList.append(inp)

                    i = 0
                    # aynı isimde değişken kullanmamaya çalış
                    for key in self.dumpFile:
                        self.dumpFile[key] = inpList[i]
                        i += 1

                    # for index2, key in enumerate(self.dumpFile):
                    #     self.dumpFile[key] = inpList[index2]

                    # güzeell
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

                    gvars.telefonlar[index].update(self.dumpFile)
                    gvars.write_phones(gvars.telefonlar)
                    break

            check = input(
                "Telefon numarasını yanlış girdiniz lütfen tekrar deneyin: ")
