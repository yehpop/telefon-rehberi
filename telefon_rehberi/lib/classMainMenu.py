from telefon_rehberi.lib.classAddNewPhoneMenu import AddNewPhoneMenu
from telefon_rehberi.lib.classEditPhoneMenu import EditPhoneMenu
from telefon_rehberi.lib.classErasePhoneMenu import ErasePhoneMenu
import telefon_rehberi.res.global_variables as gvars


class MainMenu:
    def __init__(self, menuNames: list):
        self.menuNames = menuNames
        self.__rename_menus()

        # İleride yazıyor sebebi
        self.editPhoneMenu = None
        self.newPhoneMenu = None
        self.erasePhoneMenu = None

    def __rename_menus(self):
        for index, menuName in enumerate(self.menuNames):
            self.menuNames[index] = f"{index+1}- {menuName}"

    def __print_menu(self):
        mainMenuName = "TELEFON REHBERI"

        # Biliyorum bunu ben yazdım ama utanıyorum
        maxLen = 0
        for menuName in self.menuNames:
            if len(menuName) > maxLen:
                maxLen = len(menuName)

        # Onun yerine bunu kullan daha seksi duruyor
        # max(*[len(menuName) for menuName in self.menuNames])

        offset = (maxLen - len(mainMenuName)) // 2
        # offset = maxLen/2 - len("TELEFON REHBERİ")/2
        print("\n" * 3)
        print(" " * offset, mainMenuName, " " * offset)
        print("#" * maxLen)
        print("\n".join(self.menuNames))
        print("#" * maxLen)

    def start(self):
        self.__print_menu()

        inp = "a"
        while not (inp.isdigit() and 0 < int(inp) <= len(self.menuNames)):
            inp = input("Girmek İstediğiniz Menüyü Giriniz: ")

        return self.__redirect_input(int(inp) - 1)

    def __redirect_input(self, inp: int):
        #################_REDIRECTIONS_#########################
        ########################################################
        if self.menuNames[inp].endswith("Kayıt Ekle"):
            # her seferinde yeni obje oluşturmak yerine fonksiyonları direkt statik yapabilirsin
            # pythonda class objeleri diye geçiyor
            # her seferinde yeni bir obje oluşturmamak için
            if self.newPhoneMenu is None:
                self.newPhoneMenu = AddNewPhoneMenu()
            return self.newPhoneMenu.start()
        ########################################################
        elif self.menuNames[inp].endswith("Kayıt Düzenle"):
            # ben malım neden direkt yukarıda oluşturmadım ki
            if self.editPhoneMenu is None:
                # neyse eğer kullanmadıysan daha az hafıza yiyor
                self.editPhoneMenu = EditPhoneMenu()
            return self.editPhoneMenu.start()
        ########################################################
        elif self.menuNames[inp].endswith("Kayıt Sil"):
            if self.erasePhoneMenu is None:
                self.erasePhoneMenu = ErasePhoneMenu()
            return self.erasePhoneMenu.start()
        # yapf: disable
        ########################################################
        elif self.menuNames[inp].endswith("Tüm Kayıtları Listele"):
            for index, i in enumerate(gvars.telefonlar):
                print(f"\nKayıt {index+1}: \nAdı Soyadı: {i['İsim: ']} {i['Soyisim: ']}  Telefonu: {i['Tel No: ']}\nEv Telefonu: {i['Ev No: ']}  Email Adresi: {i['Email: ']}")
            return 1
        ########################################################
        elif self.menuNames[inp].endswith("Ad veya Soyada Göre Bilgileri Getir"):
            check = str(input("Aradığınız kaydın ismini giriniz veya enter'a basınız: "))
            check2 = str(input("Aradığınız kaydın soyismini giriniz veya enter'a basınız: "))
            falseCheck = 3
            works = 0
            while not falseCheck == 0:
                print("Girdiğiniz isme sahip kayıtlar: \n")
                for index, j in enumerate(gvars.telefonlar):
                    if j['İsim: '] == check or j['Soyisim: '] == check2:
                        print(f"Adı Soyadı: {j['İsim: ']} {j['Soyisim: ']}  Telefonu: {j['Tel No: ']}  Ev Telefonu: {j['Ev No: ']}  Email Adresi: {j['Email: ']}\n")
                        works += 1
                if not works == 0:
                    return 1
                else:
                    check = input("Girdiğiniz isimde kayıt bulunamadı lütfen tekrar isim giriniz: ")
                    check2 = input("Soyisim giriniz: ")
                    falseCheck -= 1
            if falseCheck == 3:
                print("Aradığınız kayıt ya bulunmamakta ya da yanlış bilgi girmektesiniz, işlem iptal edilmiştir.")
                return 1
        ########################################################
        elif self.menuNames[inp].endswith("Telefona Göre Bilgileri Getir"):
            check = str(input("Aradığınız kaydın cep telefon numarasını giriniz veya enter'a basınız: "))
            check2 = str(input("Aradığınız kaydın ev telefon numarasını giriniz veya enter'a basınız: "))
            falseCheck = 3
            works = 0
            while not falseCheck == 0:
                print("Girdiğiniz telefonlardan birine uyan kayıtlar: \n")
                for index, j in enumerate(gvars.telefonlar):
                    if j['Tel No: '] == check or j['Ev No: '] == check2:
                        print(f"Adı Soyadı: {j['İsim: ']} {j['Soyisim: ']}  Telefonu: {j['Tel No: ']}  Ev Telefonu: {j['Ev No: ']}  Email Adresi: {j['Email: ']}\n")
                        works += 1
                if not works == 0:
                    return 1
                else:
                    check = input("Girdiğiniz numaralarla kayıt bulunamadı lütfen tekrar cep telefon numarası giriniz: ")
                    check2 = input("Ev telefon numarası giriniz: ")
                    falseCheck -= 1
            if falseCheck == 3:
                print("Aradığınız kayıt ya bulunmamakta ya da yanlış bilgi girmektesiniz, işlem iptal edilmiştir.")
                return 1
        ########################################################
        elif self.menuNames[inp].endswith("Çıkış"):
            print("Çıkış yapılıyor...")
            return False
        ########################################################
        ########################################################

# 5. ve 6. menüyü __redirect içine kodlamam kötü mü oldu emin değilim ama yeni class kurmaya değmez gibi geldi