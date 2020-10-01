import telefon_rehberi.res.global_variables as gvars
import json


class MainMenu:
    def __init__(self, menuNames: list):
        self.menuNames = menuNames
        self.__rename_menus()

    def __rename_menus(self):
        for index, menuName in enumerate(self.menuNames):
            self.menuNames[index] = f"{index+1}- {menuName}"

    def __print_menu(self):
        mainMenuName = "TELEFON REHBERI"
        maxLen = 0
        for menuName in self.menuNames:
            if len(menuName) > maxLen:
                maxLen = len(menuName)

        offset = (maxLen - len(mainMenuName)) // 2
        # offset = maxLen/2 - len("TELEFON REHBERİ")/2

        print(" " * offset, mainMenuName, " " * offset)
        print("#" * maxLen)
        print("\n".join(self.menuNames))
        print("#" * maxLen)

    def __redirect_input(self, inp: int):
        print(self.menuNames[inp])

        if self.menuNames[inp] == "Kayıt Ekle":
            addNewPhoneMenu = AddNewPhoneMenu()
            return addNewPhoneMenu.start()

    def start(self):
        self.__print_menu()

        inp = "a"
        while not (inp.isdigit() and 0 < int(inp) <= len(self.menuNames)):
            inp = input("GIRMEK ISTEDIGIN MENUYU GIR LAN: ")

        return self.__redirect_input(int(inp) - 1)
        # return True


class AddNewPhoneMenu(MainMenu):
    pass


class EditPhoneMenu(MainMenu):
    pass


def read_phones(path=gvars.jsonFilePath):
    with open(path) as file:
        read = json.load(file)
    return read


def write_phones(obj, path=gvars.jsonFilePath):
    try:
        with open(path, "w+") as file:
            json.dump(obj, file)
    except:
        return False
    return True


def main():
    mainMenuNames = [
        "Kayıt Ekle", "Kayıt Düzenle", "Kayıt Sil", "Tüm Kayıtları Listele",
        "Ad veya Soyada Göre Bilgileri Getir", "Telefona Göre Bilgileri Getir",
        "Çıkış"
    ]

    addPhoneMenuInputs = ["Telefon eklemek için gereken inputların listesi"]
    mainMenu = MainMenu(mainMenuNames)

    isRunning = True
    while isRunning:
        isRunning = mainMenu.start()


if __name__ == "__main__":
    main()
