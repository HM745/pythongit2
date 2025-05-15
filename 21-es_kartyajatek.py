import random
print("Ez a 21-es kártyajáték")
jatekmod = input("Gép vagy ember ellen szeretnél játszani?")
def gep_verzio():
    print("jétékos_lapjai:")
    jatekos = []
    jatekos.append(random.randint(2,11))
    jatekos.append(random.randint(2,11))
    print(jatekos)
    jatekos_ertek = sum(jatekos)
    print(f"Összesen:{jatekos_ertek}")
    jatekos_db = len(jatekos)
    print(f"Játékos lapjainak darab száma:{jatekos_db}")
    print("")
    print("gép lapjai:")
    gep = []
    gep.append(4)
    gep.append(6)
    print(gep)
    gep_ertek = sum(gep)
    print(f"Összesen:{gep_ertek}") 
    gep_db = len(gep)
    print(f"Gép lapjainak darab száma:{gep_db}")

def ember_verzio():
    print("játékos1 lapjai:")
    jatekos1 = []
    jatekos1.append(random.randint(2,11))
    jatekos1.append(random.randint(2,11))
    print(jatekos1)
    jatekos1_ertek = sum(jatekos1)
    print(f"Összesen:{jatekos1_ertek}")
    jatekos1_db = len(jatekos1)
    print(f"játékos1 lapjainak darab száma:{jatekos1_db}")
    print("")
    print("Játékos2 lapjai:")
    jatekos2 = []
    jatekos2.append(random.randint(2,11))
    jatekos2.append(random.randint(2,11))
    print(jatekos2)
    jatekos2_ertek = sum(jatekos2)
    print(f"Összesen:{jatekos2_ertek}")
    jatekos2_db = len(jatekos2)
    print(f"Játékos2 lapjainak darab száma:{ jatekos2_db}")

    if jatekmod == "gép":
        gep_verzio()
    elif jatekmod == "ember":
        ember_verzio()
    else:
        print("Érvénytelen játékmód.")

