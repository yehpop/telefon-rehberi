jsonFilePath = "telefon_rehberi/res/telefonlar.json"

import json


#   read_phones fonksiyonun burada durması iyi bir
# şey değil ama şimdilik sorun değil ileride taşırsın
def read_phones(path=jsonFilePath, encoding="utf-8"):
    with open(path) as file:
        read = json.load(file)
    return read

def write_phones(obj, path=jsonFilePath):
        try:
            with open(path, "w+", encoding="utf-8") as file:
                json.dump(obj, file)
        
        except:
            print("Kayıt Eklenemedi...")
            return False
        
        print("Kayıt Eklenmiştir!")
        return True

telefonlar = read_phones()