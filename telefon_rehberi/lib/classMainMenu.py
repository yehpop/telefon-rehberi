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