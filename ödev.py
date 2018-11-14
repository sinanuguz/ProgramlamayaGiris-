import numpy as np
import os
import time

os.system('COLOR 02')
os.system('mode con: cols=100 lines=25')

isim = np.empty(100, dtype='object')
yilsonuNotu = np.empty(100, dtype='object')
vize1 = np.arange(100)
vize2 = np.arange(100)
final = np.arange(100)

gecenOgrenciler = 0
kalanOgrenciler = 0
harfNotu =''

########################################

def harfNotunaCevir(nt):

    global harfNotu

    if ((nt <= 100) and (nt > 92)):
        harfNotu = "AA"
    elif ((nt > 85) and (nt <= 92)):
        harfNotu = "BA"
    elif ((nt > 78) and (nt <= 85)):
        harfNotu = "BB"
    elif ((nt > 70) and (nt <= 78)):
        harfNotu = "CB"
    elif ((nt > 65) and (nt <= 70)):
        harfNotu = "CC"
    elif ((nt > 60) and (nt <= 65)):
        harfNotu = "DC"
    elif ((nt > 55) and (nt <= 60)):
        harfNotu = "DD"
    else:
        harfNotu = "FF"


##########################################

def notOkut():

    global sinifMevcudu

    # Sınıf mevcudunu 100'e kadar almayı kontrol ettiriyor.
    sinifMevcudu = int(input("Sınıf Mevcudunu Giriniz (1-100): "))
    os.system('CLS')

    while sinifMevcudu not in range(1,101):

        print("Sınıf Mevcudu 1 ile 100 arasında olmalı !!! \n")
        sinifMevcudu = int(input("Sınıf Mevcudunu Giriniz (1-100): "))
        os.system('CLS')

    # öğrenci bilgilerini al

    for i in range(sinifMevcudu):

        # ismi al, ilk harflerini büyük harf yap...
        isim[i+1] = input("{}. öğrencinin ismini giriniz: ".format(i+1)).title()
        ad = isim[i+1]

        # 1. vize notu
        vize1[i + 1] = -1
        while not int(vize1[i+1]) in range(0, 101):
            vize1[i + 1] = int(input("{} isimli öğrencinin 1. vize notunu giriniz: ".format(ad)))


        # 2. vize notu
        vize2[i + 1] = -1
        while not int(vize2[i + 1]) in range(0, 101):
            vize2[i + 1] = int(input("{} isimli öğrencinin 2. vize notunu giriniz: ".format(ad)))

        # final notu
        final[i + 1] = -1
        while not int(final[i + 1]) in range(0, 101):
            final[i + 1] = int(input("{} isimli öğrencinin final notunu giriniz: ".format(ad)))

        harfNotunaCevir(round(vize1[i+1] * 0.2) + (vize2[i+1] * 0.2) + (final[i+1] * 0.6))

        yilsonuNotu[i + 1] = harfNotu

        time.sleep(1); os.system('CLS')

    print("Öğrenci bilgileri başarı ile alınmıştır...")
    time.sleep(2); os.system('CLS')

##############################################################

def MenuListele():

    global menuSecim

    # menüyü listele

    print("""
    ╔════════════ MENU ══════════════╗
    ║                                ║
    ║ [1] Genel Liste                ║
    ║ [2] Yıl Sonu Sınıf Ortalaması  ║
    ║ [3] Geçen Öğrenciler           ║
    ║ [4] Kalan Öğrenciler           ║  
    ║ [5] Listeyi Yenile             ║
    ║ [x] Çıkış                      ║
    ║                                ║
    ╚════════════════════════════════╝
    """)

    # seçim al.
    menuSecim = input("Seçiminiz : ")

    # yanlış bir secim yapılmısmı kontrol et
    vals = ['1','2','3','4','5','X','x']

    while menuSecim not in vals:
        print("Yanlış bir seçim yaptınız, tekrar deneyiniz !!! \n")
        menuSecim = input("Seçiminiz :")
    else:
        print("Doğru bir seçim yaptınız. \n")
        return menuSecim

##########################################################


notOkut()

secim = MenuListele()

while secim in ['1', '2', '3', '4', '5', 'x', 'X']:

    if secim == '1':    # genel liste
        input("Şimdi bütün öğrenciler listelenecek, başlamak için <enter> a basınız.\n")
        os.system('CLS')
        print("Adı\t\t\tVize1\t\tVize2\t\tFinalNotu\tDönemNotu")
        print("-"*83)

        for i in range(sinifMevcudu):
            print("{}\t\t{}\t\t{}\t\t{}\t\t{}".format(isim[i+1], vize1[i+1], vize2[i+1], final[i + 1], yilsonuNotu[i + 1]))

        input("\n\nDevam etmek için bir tuşa basınız...")
        os.system('CLS')
        secim = MenuListele()

    elif secim == '2':  # yılsonu sınıf ortalamsı

        global ortalama
        ortalama = 0


        for i in range(sinifMevcudu):
            ortalama += ((vize1[i+1] * 0.2) + (vize2[i+1] * 0.2) + (final[i+1] * 0.6))
            ortalama /= sinifMevcudu
        print("\nYıl Sonu Not Ortalaması {} dır.".format(round(ortalama,2)))

        input("\n\nDevam etmek için bir tuşa basınız...")
        os.system('CLS')
        secim = MenuListele()

    elif secim == '3':    # geçen öğrenciler
        input("Şimdi geçen öğrenciler listelenecek, başlamak için <enter> a basınız \n")
        os.system('CLS')
        print("Adı\t\t\tVize1\t\tVize2\t\tFinalNotu\tDönemNotu")
        print("-" * 83)
        gecenOgrenciler = 0

        for i in range(sinifMevcudu):
            if yilsonuNotu[i + 1] != "FF":
                print("{}\t\t{}\t\t{}\t\t{}\t\t{}".format(isim[i + 1], vize1[i + 1], vize2[i + 1], final[i + 1],
                                                          yilsonuNotu[i + 1]))
                gecenOgrenciler +=1

        print("\nGeçen Öğrenci Sayısı: {}".format(gecenOgrenciler))

        input("\n\nDevam etmek için bir tuşa basınız...")
        os.system('CLS')
        secim = MenuListele()

    elif secim == '4':    # kalan öğrenciler
        input("Şimdi kalan öğrenciler listelenecek, başlamak için <enter> a basınız \n")
        os.system('CLS')
        print("Adı\t\t\tVize1\t\tVize2\t\tFinalNotu\tDönemNotu")
        print("-" * 83)
        kalanOgrenciler = 0

        for i in range(sinifMevcudu):

            if yilsonuNotu[i + 1] == "FF":
                print("{}\t\t{}\t\t{}\t\t{}\t\t{}".format(isim[i + 1], vize1[i + 1], vize2[i + 1], final[i + 1],
                                                          yilsonuNotu[i + 1]))
                kalanOgrenciler += 1

        print("\nKalan Öğrenci Sayısı: {}".format(kalanOgrenciler))

        input("\n\nDevam etmek için bir tuşa basınız...")
        os.system('CLS')
        secim = MenuListele()

    elif secim == '5':  # listeyi yenile

        os.system('CLS')
        notOkut()

        os.system('CLS')
        secim = MenuListele()

    elif secim == 'x' or secim == 'X':   # çıkış
        os.system('CLS')
        os.system('mode con: cols=60 lines=10')

        print("""
        
            ╔════════════════════════════════╗
            ║                                ║
            ║         İyi Günler...          ║
            ║                                ║
            ╚════════════════════════════════╝
        
            """)

        time.sleep(3)
        os.system('CLS')
        break

