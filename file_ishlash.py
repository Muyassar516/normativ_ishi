
ochiril_talabalar = []
qidirilgan=[]
while True:

    print("\n🎓 Talabalar Boshqaruv Tizimi")
    print("1. Barcha talabalarni ko‘rish")
    print("2. Yangi talaba qo‘shish")
    print("3. Talabani qidirish")
    print("4. Bahoni yangilash")
    print("5. Talabani o‘chirish")
    print("6. Chiqish")
    tanlov = int(input("Tanlang (1-6): "))
    if tanlov == 1:
        try:
            with open("talabalar.txt", "r") as file:
                talabalar = file.readlines()
                if talabalar:
                    print("\n📋 Barcha talabalar:")
                    for talaba in talabalar:
                        print(talaba)
                else:
                    print("📂 Hozircha talabalar yo‘q.")

        except Exception as e:
            print(f"{e}da xatolik!!!")

    if tanlov == 2:
        try:
            id=int(input('Talabaga id kiriting: '))
            ism = input("Talabani ismini kiriting: ").title()
            fan= input(f"{ism} o'qiydigan fanni kiriting: ").lower()
            baho= int(input(f"{ism}ni bahosini kiriting: "))
            with open("talabalar.txt", "a")as file:
                file.write(f"\n{id}. {ism},fan: {fan}, bahosi: {baho}")
                print(f"{ism} ismli talaba qo'shildi")


        except Exception as e:
            print(f"{e}da xatolik!!!")

    if tanlov==3:
        try:
            u=int(input("Izlayotgan talabani id sini kiriting: "))
            with open("talabalar.txt","r") as file:
                talabalar=file.readlines()
            for talaba in talabalar:
                if talaba.startswith(f"{u}"):
                    qidirilgan.append(talaba[1])
                    print(talaba)
        except Exception as w:
            print(f"{w}da xatolik!!!")

    if tanlov==5:
        ochir=int(input("Jadvaldan o'chiriladigon talabani idsini kiriting: "))
        with open("talabalar.txt","r")as file:
            talabalar = file.readlines()
        topildi = False

        for talaba in talabalar:
            if talaba.startswith(f"{ochir}."):
                topildi = True
            else:
                ochiril_talabalar.append(talaba)

        if topildi:
            with open("talabalar.txt", "w") as file:
                file.writelines(ochiril_talabalar)
            print(f"{ochir} IDli talaba o‘chirildi!")
        else:
            print(" Bunday IDli talaba topilmadi!")
    if tanlov==6:
        print(f"{qidirilgan} qidirildi")
        print(f"{ochiril_talabalar} jadvaldan ochirildi")
        break
