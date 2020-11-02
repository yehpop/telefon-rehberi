# from telefon_rehberi.lib.classMainMenu import MainMenu
# from telefon_rehberi.lib.classMainMenu import MainMenu, telefonlar
import telefon_rehberi.res.global_variables as gvars

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
        self.dumpFile = gvars.dumpFileG

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
        check = str(input("Düzenlemek istediğiniz kaydın telefon numarasını giriniz: "))
        # yapf: enable

        # index kullanman gerekmiyor enumerate var
        inpList = []
        falseCheck = 2
        while not falseCheck == 0:
            index = -1
            # index tutarken i yerine j dersen ya da daha uzun isim kullanırsan daha iyi olur

            # for index, i in enumerate(gvars.telefonlar):
            for j in gvars.telefonlar:
                index += 1
                if j['Tel No: '] == check:
                    for i in range(len(self.addPhoneMenuInputs)):
                        inp = input(
                            "Yapmak istediğiniz değişikliği girin, yoksa Enter'a basın "
                            + self.addPhoneMenuInputs[i])
                        inpList.append(inp)

                    i = 0
                    # aynı isimde değişken kullanmamaya çalış
                    for key in self.dumpFile:
                        self.dumpFile[key] = inpList[i]
                        i += 1

                    # for index2, key in enumerate(self.dumpFile):
                    #     self.dumpFile[key] = inpList[index2]

                    # güzeell
                    # yapf: disable
                    self.dumpFile = {
                        "İsim: ": j['İsim: '] if inpList[0] == '' else inpList[0],
                        "Soyisim: ": j['Soyisim: '] if inpList[1] == '' else inpList[1],
                        "Tel No: ": j['Tel No: '] if inpList[2] == '' else inpList[2],
                        "Ev No: ": j['Ev No: '] if inpList[3] == '' else inpList[3],
                        "Email: ": j['Email: '] if inpList[4] == '' else inpList[4],
                    }
                    # yapf: enable
                    gvars.telefonlar[index].update(self.dumpFile)
                    gvars.write_phones(gvars.telefonlar)
                    gvars.telefonlar = gvars.read_phones()
                    print("Kayıttaki değişiklikler kaydedildi...")
                    return 1
            # yapf: disable

            # burası çalışabiliyorsa for döngüsünde bir şeyler yanlış gitmiştir
            # ve bu da muhtemelen telefon numarasının yanlış girildiğini gösterir
            # bunu kullanıcıya bildirip tel nosunun tekrar girilmesi istenir
            # ve for loop'u yeniden çalışır

            check = input("Telefon numarasını yanlış girdiniz lütfen tekrar deneyin: ")
            falseCheck -= 1
        # burası ise ancak while loop'unda bir sorun olduğunda veya loop durduğunda çalışacaktır
        # loop'un durması 3 kez yanlış numara girildiğinde gerçekleşir
        print("Telefon numarasını çok kez yanlış girdiğiniz için işlem iptal edilmiştir.")
        return 1 # ana menüye dönmek için
        # yapf: enable
