from telefon_rehberi.main import write_phones, read_phones
from telefon_rehberi.lib.classMainMenu import MainMenu


class AddNewPhoneMenu(MainMenu):
    def addPhone(self):
        write_phones(self)