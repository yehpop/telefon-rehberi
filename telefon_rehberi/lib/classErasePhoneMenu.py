import telefon_rehberi.res.global_variables as gvars


class ErasePhoneMenu:
    def __init__(self):
        self.addPhoneMenuInputs = [
            "İsim: ", "Soyisim: ", "Tel No: ", "Ev No: ", "Email: "
        ]
        self.dumpFile = gvars.dumpFileG

    def print_menu(self):
        # yapf: disable
        print("\n############################################\nTelefon Kaydı Silme Menüsüne Hoşgeldiniz...\n############################################")
        # yapf: enable

    def start(self):
        self.print_menu()

        # yapf: disable
        check = str(input("Silmek istediğiniz kaydın telefon numarasını giriniz: "))
        # yapf: enable

        falseCheck = 2
        while not falseCheck == 0:
            for index, j in enumerate(gvars.telefonlar):
                if j['Tel No: '] == check:
                    # yapf: disable
                    authorization = 0
                    while authorization == 0:
                        authorize = input(f"'{j['İsim: ']} {j['Soyisim: ']}' isimli kaydı silmek istediğinize emin misiniz?\n evet veya hayır ile cevap verin (e/h) ")
                        if authorize.lower() == 'e':
                            gvars.telefonlar.pop(index)
                            gvars.write_phones(gvars.telefonlar)
                            print("Kayıt silindi...")
                            return 1
                        elif authorize.lower() == 'h':
                            print("İşlem iptal edildi.")
                            return 1
                        else:
                            print("Lütfen evet için 'e' hayır için 'h' yazınız...")
            # bu kısmı classEditPhoneMenu.py dosyasında açıkladm
            check = input("Telefon numarasını yanlış girdiniz lütfen tekrar deneyin: ")
            falseCheck -= 1
        print("Telefon numarasını çok kez yanlış girdiğiniz için işlem iptal edilmiştir.")
        return 1    # yapf: enable
