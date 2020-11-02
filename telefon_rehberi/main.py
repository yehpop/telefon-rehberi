from telefon_rehberi.lib.classMainMenu import MainMenu


def main():
    mainMenuNames = [
        "Kayıt Ekle", "Kayıt Düzenle", "Kayıt Sil", "Tüm Kayıtları Listele",
        "Ad veya Soyada Göre Bilgileri Getir", "Telefona Göre Bilgileri Getir",
        "Çıkış"
    ]

    mainMenu = MainMenu(mainMenuNames)

    isRunning = True
    while isRunning:
        isRunning = mainMenu.start()


# if __name__ == "__main__":
#     main()