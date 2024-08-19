import random

def tas_kagit_makas_busra_sevindik():
    def pc_secimi_uret():
        secenekler = ["tas", "kagit", "makas"]
        return random.choice(secenekler)

    def pc_oynama_istegi():
        return random.choice(["evet", "hayir"])

    def oyunu_oyna():
        kullanici_tur = 0
        pc_tur = 0
        tur_numarasi = 1

        while kullanici_tur < 2 and pc_tur < 2:  # 2 tur kazanan olana kadar devam edecek
            kullanici_skor = 0
            pc_skor = 0

            print(f"\n--- {tur_numarasi}. Tura Başlıyoruz! ---")  # Kaçıncı tura başlandığını gösteren mesaj

            while kullanici_skor < 2 and pc_skor < 2:  # Her turda 2 sayıya ulaşana kadar devam edecek
                kullanici_secimi = input("Tas? Kagit? Makas? ").lower()

                while kullanici_secimi not in ["tas", "kagit", "makas"]:
                    print("Geçersiz seçim! Lütfen 'tas', 'kagit' veya 'makas' giriniz.")
                    kullanici_secimi = input("Tas? Kagit? Makas? ").lower()

                pc_secimi = pc_secimi_uret()
                print("Bilgisayar: ", pc_secimi)

                if pc_secimi == kullanici_secimi:
                    print("Berabere!")
                elif (pc_secimi == "tas" and kullanici_secimi == "kagit") or \
                    (pc_secimi == "kagit" and kullanici_secimi == "makas") or \
                    (pc_secimi == "makas" and kullanici_secimi == "tas"):
                    kullanici_skor += 1
                    print("Bu turu siz kazandınız!")
                else:
                    pc_skor += 1
                    print("Bu turu bilgisayar kazandı!")

                print("Durum: Siz {} - Bilgisayar {}".format(kullanici_skor, pc_skor))

            if kullanici_skor == 2:
                kullanici_tur += 1
                print("Tebrikler! Bu turu siz kazandınız!")
            elif pc_skor == 2:
                pc_tur += 1
                print("Bu turu bilgisayar kazandı.")

            print("Genel Durum: Siz {} - Bilgisayar {}".format(kullanici_tur, pc_tur))
            tur_numarasi += 1  # Tur numarasını artırıyorum

        if kullanici_tur > pc_tur:
            print("***TEBRİKLER! OYUNU SİZ KAZANDINIZ!***")
        else:
            print("MAALESEF! OYUNU BİLGİSAYAR KAZANDI:)).")

    # Oyunun kuralları ve giriş mesajı
    print("*****Taş Kağıt Makas Oyununa Hoşgeldin!*****")
    print("***Oyunun Kuralları***")
    print("- Taş makası yener")
    print("- Makas kağıdı yener")
    print("- Kağıt taşı yener")
    print("- Toplamda 3 tur oynanacak")
    print("- 2 tur kazanan oyunun galibi olacak")
    print("- Şunu unutmayın!! Siz oyun oynamak isteseniz \nbile bazen bilgisayarımız oyun oynamak\n"
          "istemeyebilir lütfen onu da anlayışla karşılayın:)")

    while True:
        # Kullanıcıya ve bilgisayara oynamak isteyip istemediğini soruyorum
        kullanici_choice = input("Oyuna başlamak istiyor musunuz? (Evet/Hayır): ").lower()

        while kullanici_choice not in ["evet", "hayır"]:
            print("Geçersiz seçim! Lütfen 'evet' veya 'hayir' yazınız.")
            kullanici_choice = input("Oyuna başlamak istiyor musunuz? (Evet/Hayır): ").lower()

        pc_oynuyor = pc_oynama_istegi()


        if kullanici_choice == "evet" and pc_oynuyor == "evet":
            print("Bilgisayar da oynamak istiyor. Oyun başlıyoooor!")
            oyunu_oyna()
        elif kullanici_choice == "hayır":
            print("Başlamadan bitirdik:(( Başka zaman oynamak istersen, yine beklerim!")
            break
        else:
            print("Bilgisayar oyun oynamak istemiyooorr. Oyun sona erdii:))")
            break

        # Oyun sonunda tekrar oynamak isteyip istemediklerini soruyorum
        kullanici_tekrar_oyna = input("Tekrar oynamak ister misiniz? (Evet/Hayır): ").lower()
        pc_tekrar_oynuyor = pc_oynama_istegi()

        if kullanici_tekrar_oyna!= "evet" or pc_tekrar_oynuyor != "evet":
            print("Birileri tekrar oynamak istemiyoor :) Tekrar görüşmek üzere!!")
            break

tas_kagit_makas_busra_sevindik()
