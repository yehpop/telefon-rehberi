import json
import telefon_rehberi.res.global_variables as gvars

# kardeşim ne yaptın
# from telefon_rehberi.lib.classMainMenu import MainMenu, telefonlar

# Olmadı bu
# class AddNewPhoneMenu(MainMenu):
# inheritance için main menuyu değil basemenu tarzında bir şey kullan eğer yapacaksan

#   şimdi MainMenuden inheritlemeye çalıştığımızda hata
# alıyoruz çünkü MainMenu'nün bu classlara erişebilmesi gerekiyor
# __redirect filan hani

# Ayrıca kodunu biraz daha açıklamaya çalış


# eğer o işlere girersen interface ve metaclasslara da bak
class AddNewPhoneMenu:
    def __init__(self):
        self.addPhoneMenuInputs = [
            "İsim: ", "Soyisim: ", "Tel No: ", "Ev No: ", "Email: "
        ]
        self.dumpFile = gvars.dumpFileG

    def print_menu(self):
        maxLenA = 0
        for menu in self.addPhoneMenuInputs:
            if len(menu) > maxLenA:
                maxLenA = len(menu)
        offset = int(maxLenA / 2 -
                     len("Yeni Telefon Kaydı Ekleme Menüsüne Hoşgeldiniz!") /
                     2)
        # yapf: disable
        print("\n" * 3 + " " * offset +
            "Yeni Telefon Kaydı Ekleme Menüsüne Hoşgeldiniz!" +
            " " * offset,
            "\n" +
            "#" * len(" " * offset + "Yeni Telefon Kaydı Ekleme Menüsüne Hoşgeldiniz!" + " " * offset))
        # yapf: enable

    # def redirect_input(self, inp: int):
    #   print(self.addPhoneMenuInputs[inp])

    def start(self):
        self.print_menu()

        inpList = []
        for i in range(len(self.addPhoneMenuInputs)):
            inp = input(self.addPhoneMenuInputs[i])
            inpList.append(inp)

        # böyle yapmana gerek yok
        # i = 0
        # for key in self.dumpFile:
        #     self.dumpFile[key] = inpList[i]
        #     i += 1

        # bu daha python
        for i, key in enumerate(self.dumpFile):
            self.dumpFile[key] = inpList[i]

        print(self.dumpFile)
        gvars.telefonlar.append(self.dumpFile)
        gvars.write_phones(gvars.telefonlar)
        gvars.telefonlar = gvars.read_phones()
        print("Kayıt eklenmiştir!..")
        return 1