
"""

  "Python ile Basit Oyunlar"
  Developer Mavi16

"""

# "Zaman" kütüphanesini çağırıyoruz.
import time


def amiralBattiOyunu():

    # Gerekli kütüphaneyi çağırıyoruz.
    from random import randint

    # Gereken tanımlamaları yapıyoruz.
    board = []
    sayac = 0
    puan = 250

    for i in range(5):
        board.append(["0"] * 5)

    def print_board(board):
        for satir in board:
            print(" ".join(satir))

    def rand(board):
        return randint(1, len(board) - 1)

    print("-" * 35)
    print("Amiral battı oyununa hoş geldiniz")
    print("-" * 35)
    print("Puanınız:", puan)
    print("-" * 35)
    print_board(board)
    gemi_satir = rand(board)
    gemi_sutun = rand(board)
    gemi1_satir = rand(board)
    gemi1_sutun = rand(board)
    gemi2_satir = rand(board)
    gemi2_sutun = rand(board)
    while True:
        if (gemi_satir == gemi1_satir and gemi_sutun == gemi1_sutun):
            gemi1_satir = rand(board)
            gemi1_sutun = rand(board)
            continue
        elif (gemi_satir == gemi2_satir and gemi_sutun == gemi2_sutun):
            gemi2_satir = rand(board)
            gemi2_sutun = rand(board)
            continue
        elif (gemi1_satir == gemi2_satir and gemi1_sutun == gemi2_sutun):
            gemi2_satir = rand(board)
            gemi2_sutun = rand(board)
            continue
        else:
            print("-" * 35)
            tahmin_satir = int(input("Satır giriniz: "))
            tahmin_sutun = int(input("Sütun giriniz: "))
            if (tahmin_satir == gemi_satir and tahmin_sutun == gemi_sutun) \
                    or (tahmin_satir == gemi1_satir and tahmin_sutun == gemi1_sutun) \
                    or (tahmin_satir == gemi2_satir and tahmin_sutun == gemi2_sutun):
                if board[tahmin_satir - 1][tahmin_sutun - 1] == "/":
                    print("-" * 35)
                    print("Zaten tahmin ettiniz")
                    print_board(board)
                    print(puan)
                else:
                    print("-" * 35)
                    print("Tebrikler gemiyi batırdınız!")
                    board[tahmin_satir - 1][tahmin_sutun - 1] = "/"
                    print("Puanınız:", puan)
                    print("-" * 35)
                    print_board(board)
                    sayac += 1
            else:
                if (tahmin_satir < 0 or tahmin_sutun < 0) or (tahmin_satir > 5 or tahmin_sutun > 5):
                    print("-" * 35)
                    print("Alan sınırları dışında değer girdiniz")
                elif board[tahmin_satir - 1][tahmin_sutun - 1] == "X":
                    print("-" * 35)
                    print("Zaten tahmin ettiniz")
                    print("-" * 35)
                    print_board(board)
                else:
                    print("-" * 35)
                    print("Vuramadınız")
                    board[tahmin_satir - 1][tahmin_sutun - 1] = "X"
                    puan -= 10
                    print("Puanınız:", puan)
                    print("-" * 35)
                    print_board(board)
                if sayac == 3:
                    print("-" * 35)
                    print("Tebrikler bütün gemileri batırdınız ve oyunu kazandınız")
                    print("-" * 35)
                    break


# Gerekli kütüphaneleri çağırıyoruz
import random
import time

class BasitTasKagitMakasOyunu():

    def __init__(self):
        self.secim()

    def secim(self):
        baslik = "Taş Kağıt Makas Oyunu Oynama"
        print("*" * len(baslik), baslik, "*" * len(baslik), sep="\n", end="\n")
        while True:
            tercih = input("Oyunun açıklaması için 1'e oyuna giriş için 2'ye basınız :")

            if tercih == "1":
                self.oyunAciklamasi()
            elif tercih == "2":
                self.tasKagitMakasOyunu()
                break
            else:
                print("Geçersiz bir karaktere bastınız.. İşleminiz İPTAL ediliyor..")
                break

    def oyunAciklamasi(self):
        print("""Oyunun Açıklaması = >
    Klasik taş kağıt makas oyunu. 
    Kullanıcının seçim yaptığı andaki bilgisayarın kullandığıyla kullanıcının seçtiği karşılaştırılıyor. 
    Oyun, kullanıcı seçim ekranında 1 veya TAŞ, 2 VEYA KAĞIT, ya da 3 VEYA MAKAS dışında 
    bir veri girene kadar devam ediyor.
    """)

    def tasKagitMakasOyunu(self):

        durumlar = ["TAŞ", "KAĞIT", "MAKAS", "1", "2", "3"]

        while True:
            kullanıcı = input("1){}\n2){}\n3){}\nSeçiniz =>".format(*durumlar)).upper()
            bilgisayar = random.randrange(0, 3)
            sayı = -1

            if kullanıcı in durumlar:
                if kullanıcı == "1" or kullanıcı == "TAŞ":
                    sayı = 0

                elif kullanıcı == "2" or kullanıcı == "KAĞIT":
                    sayı = 1

                elif kullanıcı == "3" or kullanıcı == "MAKAS":
                    sayı = 2

                if sayı == bilgisayar:
                    print("Berabere, sen {} yaptın = ben {} yaptım".format(durumlar[sayı], durumlar[bilgisayar]))

                elif sayı == 0 and bilgisayar == 2:
                    print("Sen kazandın, sen {} yaptın = ben {} yaptım".format(durumlar[sayı], durumlar[bilgisayar]))

                elif sayı == 0 and bilgisayar == 1:
                    print("Ben kazandım, sen {} yaptın = ben {} yaptım".format(durumlar[sayı], durumlar[bilgisayar]))

                elif sayı == 1 and bilgisayar == 2:
                    print("Ben kazandım, sen {} yaptın = ben {} yaptım".format(durumlar[sayı], durumlar[bilgisayar]))

                elif sayı == 1 and bilgisayar == 0:
                    print("Sen kazandın, sen {} yaptın = ben {} yaptım".format(durumlar[sayı], durumlar[bilgisayar]))

                elif sayı == 2 and bilgisayar == 1:
                    print("Sen kazandın, sen {} yaptın = ben {} yaptım".format(durumlar[sayı], durumlar[bilgisayar]))

                elif sayı == 2 and bilgisayar == 0:
                    print("Ben kazandım, sen {} yaptın = ben {} yaptım".format(durumlar[sayı], durumlar[bilgisayar]))

                print()
            else:
                print("Oyun Bitiriliyor :(")
                break


def kelimeOyunu():

    # Kullanıcının rastgele seçilen bir kelimeyi tahmin ettiği bir oyun yapabilirsiniz.
    # Kullanıcıya ipucu vererek harf tahminleri yapmasına olanak sağlayabilirsiniz.

    import random

    def choose_word():
        words = [input("Tahmin edilecek kelimeyi girin (boşluk bırakmayın): ")]
        return random.choice(words)

    def play_game(word):
        guessed_letters = []
        max_attempts = 5
        attempts = 0

        while attempts < max_attempts:
            print("Kelime: ", end="")
            for letter in word:
                if letter in guessed_letters:
                    print(letter, end="")
                else:
                    print("_", end="")
            print()

            if len(guessed_letters) > 0:
                print("Tahmin Edilen Harfler: ", end="")
                print(", ".join(guessed_letters))

            guess = input("Bir harf tahmin edin: ").lower()

            if len(guess) != 1:
                print("Yanlış giriş. Tek bir harf girin.")
                continue

            if guess in guessed_letters:
                print("Bu harfi zaten tahmin ettiniz.")
                continue

            guessed_letters.append(guess)

            if guess in word:
                print("Doğru tahmin!")
                if all(letter in guessed_letters for letter in word):
                    print("Tebrikler, kelimeyi doğru tahmin ettiniz!")
                    break
            else:
                print("Yanlış tahmin!")
                attempts += 1

        if attempts == max_attempts:
            print("Maalesef, tahmin hakkınız bitti. Doğru kelime: ", word)

    word = choose_word()
    play_game(word)


def zarAtmaOyunu():

    # Gereken kütüphaneleri çağırıyoruz.
    import random
    import time

    i = 1
    while True:
        zar_1 = random.randint(1, 6)
        zar_2 = random.randint(1, 6)

        if zar_1 == 6 and zar_2 == 6:
            print("""Deneme {}:\t({},{}) *** """.format(i, zar_1, zar_2))
            time.sleep(2)
            break

        print("""Deneme {}:\t({},{}) """.format(i, zar_1, zar_2))
        i += 1
        time.sleep(0.5)

    print("""\n*** {}. denemede (6,6) geldi ***""".format(i))

def sayiTahminOyunu():

    # Gerekli kütüphaneyi çağırıyoruz.
    from random import randint

    rand = randint(1, 100)
    sayac = 0

    while True:
        sayac += 1
        sayi = int(input("1 ile 100 arasında değer girin (0 çıkış):"))
        if (sayi == 0):
            print("Oyunu iptal Ettiniz")
            break
        elif sayi < rand:
            print("Daha yüksek bir değer girin.")
            continue
        elif sayi > rand:
            print("Daha düşük bir sayı girin.")
            continue
        else:
            print("Rastgele seçilen sayı {0}!".format(rand))
            print("Tahmin sayınız {0}".format(sayac))


print("1. Amiral Battı Oyunu \n2. Taş Kağıt Makas Oyunu \n3. Kelime Tahmin Oyunu \n4. Zar Atma Oyunu \n5. Sayı Tahmin Oyunu")
secim = int(input("Seçiminizi yapın (1-5): "))


if secim == 1:
    print("Oyuna yönlendiriliyorsunuz...")
    time.sleep(3)
    amiralBattiOyunu()

elif secim == 2:
    print("Oyuna yönlendiriliyorsunuz...")
    time.sleep(3)
    BasitTasKagitMakasOyunu()

elif secim == 3:
    print("Oyuna yönlendiriliyorsunuz...")
    time.sleep(3)
    kelimeOyunu()

elif secim == 4:
    print("Oyuna yönlendiriliyorsunuz...")
    time.sleep(3)
    zarAtmaOyunu()

elif secim == 5:
    print("Oyuna yönlendiriliyorsunuz...")
    time.sleep(3)
    sayiTahminOyunu()

else:
    print("Hatalı seçim, lütfen '1-2-3-4-5' gibi bir rakam girin..!")