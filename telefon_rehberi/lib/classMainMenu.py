import json
import telefon_rehberi.res.global_variables as gvars


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
        print("\n" * 3)
        print(" " * offset, mainMenuName, " " * offset)
        print("#" * maxLen)
        print("\n".join(self.menuNames))
        print("#" * maxLen)

    def __redirect_input(self, inp: int):
        rd = inp + 1
        if not rd == 1 or rd == 7:
            print(self.menuNames[inp])
        return rd

    def start(self):
        self.__print_menu()

        inp = "a"
        while not (inp.isdigit() and 0 < int(inp) <= len(self.menuNames)):
            inp = input("GIRMEK ISTEDIGIN MENUYU GIR LAN: ")

        return self.__redirect_input(int(inp) - 1)
        # return True


def read_phones(path=gvars.jsonFilePath):
    with open(path) as file:
        read = json.load(file)
    return read


telefonlar = read_phones()