print("Zadanie 6")
droga = float(input("Napisz długość drogi: "))
spalanie = float(input("Napisz średnie spalanie w litrach na 100km: "))
cena_za_litr = 6.5
zuzycie_paliwa = droga * (spalanie / 100)
koszt = zuzycie_paliwa * cena_za_litr
print(f"Szacowane zużycie paliwa wynosi:  {zuzycie_paliwa} ,a szacowane koszta wynoszą{koszt}")

print("zadanie 6a,6b")
import random
droga2 = random.randint(0, 100)
spalanie2 = float(input("Napisz średnie spalanie w litrach na 100km: "))
cena_za_litr2 = float(input("Napisz aktualną cenę paliwa za litr: "))
zuzycie_paliwa2 = droga2 * (spalanie2 / 100)
koszt2 = zuzycie_paliwa2 * cena_za_litr2
print(f"Szacowane zużycie paliwa wynosi:  {zuzycie_paliwa2} ,a szacowane koszta wynoszą{koszt2}")
