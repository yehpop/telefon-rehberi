import json
import telefon_rehberi.res.global_variables as gvars
from telefon_rehberi.lib.classMainMenu import MainMenu


class AddNewPhoneMenu(MainMenu):
    def addPhone(self):
        pass


def write_phones(obj, path=gvars.jsonFilePath):
    try:
        with open(path, "w+") as file:
            json.dump(obj, file)
    except:
        return False
    return True
