jsonFilePath = "telefon_rehberi/res/telefonlar.json"

import json


# read_phones fonksiyonun burada durması iyi bir
# şey değil ama şimdilik sorun değil ileride taşırsın
def read_phones(path=jsonFilePath):
    with open(path) as file:
        read = json.load(file)
    return read


def write_phones(obj, path=jsonFilePath):
    try:
        with open(path, "w+") as file:
            json.dump(obj, file, indent=4)
    except:
        print("İşlem başarısız...")
        return False
    return True


telefonlar = read_phones()

dumpFileG = {
    "İsim: ": None,
    "Soyisim: ": None,
    "Tel No: ": None,
    "Ev No: ": None,
    "Email: ": None
}
