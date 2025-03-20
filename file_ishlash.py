savat=[]
buyurtmalar=[]
class Dish:
    dishes = []

    def __init__(self, nomi, tavsifi, narxi):
        self.nomi = nomi
        self.tavsifi = tavsifi
        self.narxi = narxi

    def jami(self):
        return Dish.dishes.append(self)

    @classmethod
    def show_products(cls, nom):
          savat = []
          for dish in Dish.dishes:
              if dish.nom == nom:
                  savat.append(dish)

          return savat


class Ochirish:
    def __init__(self,ochiradigon):
        self.ochiradigon=ochiradigon
    def ochirgan(self):
        return  ochirilash


class Menu(Dish):
    def __init__(self,nomi, tavsifi, narxi):
        Dish.show_products(dish)
        super().__init__(nomi,tavsifi,narxi)


    @classmethod
    def show_menu(cls):
        if savat=='':
            print("Menyu bo'sh!")
        else:
            print("=== Menyu ===")
            for dish in cls.dishes:
                print(f"Taom: {dish.nomi}, Tavsif: {dish.tavsifi}, Narx: {dish.narxi} so'm")


class Buyurtma(Dish):
    def __init__(self,nomi,tavsifi,narxi):
        Dish.show_products(dish)
        super().__init__(nomi,tavsifi,narxi)
    def buyurtmacha(self):
        return buyurtmalar


while True:
    print("\n1. yangi taom qo'shish")
    print("2. taomni o'chirish")
    print("3. menyuni ko'rish ")
    print("4. buyurtma qilish")
    print("5. dasturdan chiqish")

    tanlov = int(input('Tanlov kiriting(1-5): '))
    if tanlov == 1:
        nomi = input("yangi taom nomini kiriting: ")
        tavsifi = input(f"{nomi}ni tavsifini kiriting: ")
        narxi = int(input(f"{nomi}ni narxini kiriting:"))
        dish=(nomi,tavsifi,narxi)
        # Dish(nomi, tavsifi, narxi)

        new_dish = Dish(nomi, tavsifi, narxi)
        new_dish.show_products(nomi)
        savat.append(nomi)
        print(f"{nomi} taomi muvaffaqiyatli qo'shildi.")

    if tanlov==2:
        # Dish.show_products(dish)
        ochirilash = input("qaysi taomni o'chirmoqchisiz?")
        if not ochirilash in savat:
            print("bunday taom menyuda yo'q !")
        else:
            savat.remove(ochirilash)
            print(f"menyuda {ochirilash} o'chirildi")

    elif tanlov==3:
        Menu.show_menu()
        print(savat)
        print("jarayon tugadi")

    elif tanlov==4:
        while True:
            buyurtma=input("nima buyurtma qilmoqchisiz? ")
            if not buyurtma in savat:
                print("bunday taom menyuda yo'q")
            else:
                buyurtmalar.append(buyurtma)
                print(f"sizning buyurtmangiz {buyurtmalar}")

            keyingi=input('yana buyurtma qilmoqchimisiz? ')
            if keyingi=='ha':
                continue
            else:
                print(f"sizning buyurtmangiz: {buyurtmalar}")
                break
    elif tanlov==5:
        break
