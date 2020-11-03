import telefon_rehberi.res.global_variables as gvars


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

    def start(self):
        self.print_menu()

        inpList = []
        for i in range(len(self.addPhoneMenuInputs)):
            inp = input(self.addPhoneMenuInputs[i])
            inpList.append(inp)
        # bu daha python
        for i, key in enumerate(self.dumpFile):
            self.dumpFile[key] = inpList[i]
        # eklenmek istenen kaydın bilgileri alınıp bi listeye konuluyor sonra bu listenin
        # üyeleri tek tek dumpFile sözlüğüne ekleniyo ilk üye ilk anahtara ikinci üye ikinci üyeye
        # şeklinde sonra sözlük telefonlar değişkenine atanıyor ve telefonlar telefonlar.json'a yazılıyo
        # en sondaki gvars.telefonlar = gvars.read_phones() olmasaydı çıkış yapmadan birden çok kayıt
        # ekleddiğinde tüm kayıtlara en son girdiğin bilgiler yazılıyor.
        print(self.dumpFile)
        gvars.telefonlar.append(self.dumpFile)
        gvars.write_phones(gvars.telefonlar)
        gvars.telefonlar = gvars.read_phones()
        print("Kayıt eklenmiştir!..")
        return 1