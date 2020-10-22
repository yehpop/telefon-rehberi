from telefon_rehberi.lib.classAddNewPhoneMenu import AddNewPhoneMenu
from telefon_rehberi.lib.classEditPhoneMenu import EditPhoneMenu
import telefon_rehberi.res.global_variables as gvars


class MainMenu:
    def __init__(self, menuNames: list):
        self.menuNames = menuNames
        self.__rename_menus()

        # İleride yazıyor sebebi
        self.editPhoneMenu = None
        self.newPhoneMenu = None

    def __rename_menus(self):
        # Burada değişen değişken farklı bir şey olsa iyi olur
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

    def __redirect_input(self, inp: int):
        # rd kullanmana gerek yok
        rd = inp + 1
        if rd != 1 or rd == 7:  # yapılacak çok şey var
            print(self.menuNames[inp])
        
        #           neden kaçıncı menüyü seçtiğimizi döndürdüğünü anlayamadım 
        #       zaten bu fonksiyonun meselesi kaçıncıyı işlediğimize göre tepki 
        #   vermekti. yani ifler içinde diğermenü.start() yapıp onların döndürdüğü 
        # değeri döndürmen lazım (Eğer çıkışa dair bir şey yapılmadıysa onlar da True döndürecek)

        #   örnek olarak if False içine 
        # yazacağım istersen çıkarırsın
        if False:
            # mainMenuNames = [
            #     "Kayıt Ekle", "Kayıt Düzenle", "Kayıt Sil", "Tüm Kayıtları Listele",
            #     "Ad veya Soyada Göre Bilgileri Getir", "Telefona Göre Bilgileri Getir",
            #     "Çıkış"
            # ]
            
            # endswith yapma sebebim sayıların çıkmasını istememem
            # index yerine yazıyı kontrol etme sebebim de okunabilirlik filan
            if self.menuNames[inp].endswith("Kayıt Ekle"):
                # her seferinde yeni obje oluşturmak yerine fonksiyonları direkt statik yapabilirsin
                # pythonda class objeleri diye geçiyor
                # her seferinde yeni bir obje oluşturmamak için
                if self.newPhoneMenu is None:
                    self.newPhoneMenu = AddNewPhoneMenu()
                return self.newPhoneMenu.start()
            
            elif self.menuNames[inp].endswith("Kayıt Düzenle"):
                ##################################################
                # ben malım neden direkt yukarıda oluşturmadım ki
                ##################################################
                
                if self.editPhoneMenu is None:
                    # neyse eğer kullanmadıysan daha az hafıza yiyor
                    self.editPhoneMenu = EditPhoneMenu()
                return self.editPhoneMenu.start()
            
            elif self.menuNames[inp].endswith("Çıkış"):
                return False

        return rd

    def start(self):
        self.__print_menu()

        inp = "a"
        while not (inp.isdigit() and 0 < int(inp) <= len(self.menuNames)):
            inp = input("GIRMEK ISTEDIGIN MENUYU GIR LAN: ")

        return self.__redirect_input(int(inp) - 1)
        # return True

# olmaaaazzzz
# bunu daha farklı bir yere alalım
# herkeste olması sorun olmayacak bir yer gibi bir yer 
# hömmmm
# global_variables hoş mesela

# def read_phones(path=gvars.jsonFilePath):
#     with open(path) as file:
#         read = json.load(file)
#     return read


# telefonlar = read_phones()