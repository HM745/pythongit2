import random
print("Ez a 21-es kártyajáték")
jatekmod = input("Gép vagy ember ellen szeretnél játszani?(gép/ember)")

def gep_verzio():
    print("Játékos lapjai:")
    jatekos = []
    jatekos.append(random.randint(2,11))
    jatekos.append(random.randint(2,11))
    print(jatekos)
    jatekos_ertek = sum(jatekos)
    print(f"Összesen:{jatekos_ertek}")
    jatekos_db = len(jatekos)
    print(f"Játékos lapjainak darab száma:{jatekos_db}")
    print("")
    print("Gép lapjai:")
    gep = []
    gep.append(4)
    gep.append(6)
    print(gep)
    gep_ertek = sum(gep)
    print(f"Összesen:{gep_ertek}") 
    gep_db = len(gep)
    print(f"Gép lapjainak darab száma:{gep_db}")
    print("")
    uj_lap = input("Szeretnél húzni mégegy lapot?(igen/nem)")
    if uj_lap == "igen":
        jatekos.append(random.randint(2,11))
        print("")
        print(f"Új lappal együtt a lapjaid:{jatekos}")
        jatekos_ertek = sum(jatekos)
        jatekos_db = len(jatekos)
        print(f"Így összesen:{jatekos_ertek}")
        print(f"Kártyáid darab száma:{jatekos_db}")
    elif uj_lap == "nem":
        print("")
        print("Nem huztál új lapot, így a lapjaid értéke nem változott")
    else:
        print("")
        print("Nem érvényes választás")
    if gep_ertek == 21:
        print("")
        print("Eredmények:")
        print("")
        print("✅A gép nyert✅")
    elif jatekos_ertek == 21:
        print("")
        print("Eredmények:")
        print("")
        print("✅Nyertél✅")
    elif gep_ertek > 21:
        print("")
        print("Eredmények:")
        print("")
        print("🔴Túl mentél a 21-nél🔴")
        print("❌Vesztettél❌")
    elif jatekos_ertek > 21:
        print("")
        print("Eredmények:")
        print("")
        print("🔴Túl mentél a 21-nél🔴")
        print("")
        print("❌Vesztettél❌")
    elif jatekos_ertek > gep_ertek:
        print("")
        print("Eredmények:")
        print("")
        print("✅Nyertél✅")
    elif jatekos_ertek < gep_ertek:
        print("")
        print("Eredmények:")
        print("")
        print("❌Vesztettél❌")
    elif gep_ertek == jatekos_ertek:
        print("")
        print("Eredmények:")
        print("")
        print("🕒Döntetlen, játsz újra🕒")


def ember_verzio():
    print("Játékos1 lapjai:")
    jatekos1 = []
    jatekos1.append(random.randint(2,11))
    jatekos1.append(random.randint(2,11))
    print(jatekos1)
    jatekos1_ertek = sum(jatekos1)
    print(f"Összesen:{jatekos1_ertek}")
    jatekos1_db = len(jatekos1)
    print(f"Játékos1 lapjainak darab száma:{jatekos1_db}")
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
    print("")
    jatekos1_uj_lap = input("Játékos 1 Szeretnél mégegy új lapot húzni?(igen/nem)")
    print("")
    jatekos2_uj_lap = input("Játékos 2 Szeretnél mégegy új lapot húzni?(igen/nem)")
    if jatekos1_uj_lap == "igen":
        jatekos1.append(random.randint(2,11))
        print("")
        print(f"Játékos 1 új lapot húzott, így a lapjai:{jatekos1}")
        jatekos1_ertek = sum(jatekos1)
        jatekos1_db = len(jatekos1)
        print(f"Így játékos 1 lapjai összesen:{ jatekos1_ertek}")
        print(f"Játékos 1 kártyainak a darab száma:{jatekos1_db}")
    elif jatekos1_uj_lap == "nem":
        print("")
        print("Játékos 1 lapjai nem változtak, mivel nem húzott új lapot")
    else: 
        print("")
        print("Nem érvényes választás")
    if jatekos2_uj_lap == "igen":
        jatekos2.append(random.randint(2,11))
        print("")
        print(f"Játékos 2 új lapot húzott, így a lapjai:{jatekos2}")
        jatekos2_ertek = sum(jatekos2)
        jatekos2_db = len(jatekos2)
        print(f"Így játékos 2 lapjai összesen:{jatekos2_ertek}")
        print(f"Játékos 2 kártyainak a darab száma:{jatekos2_db}")
    elif jatekos2_uj_lap == "nem":
        print("")
        print("Játékos 2 lapjai nem változtak, mivel nem húzott új lapot")
    else:
        print("")
        print("Nem érvényes választás")
    if jatekos1_ertek == 21:
        print("")
        print("Eredmények:")
        print("")
        print("✅Játékos1 nyert✅")
        print("")
        print("❌Játékos2 veszett❌")
    elif jatekos2_ertek == 21:
        print("")
        print("Eredmények:")
        print("")
        print("✅Játékos2 nyert✅")
        print("")
        print("❌Játékos1 vesztett❌")
    elif jatekos1_ertek > 21:
        print("")
        print("Eredmények:")
        print("")
        print("🔴Játékos1 Túl ment 21-nél🔴")
        print("")
        print("✅Játékos2 nyert✅")
        print("")
        print("❌Játékos1 vesztett❌")
    elif  jatekos2_ertek > 21:
        print("")
        print("Eredmények:")
        print("")
        print("🔴Játékos1 Túl ment 21-nél🔴")
        print("")
        print("✅Játékos2 nyert✅")
        print("")
        print("❌Játékos1 vesztett❌")
    elif jatekos1_ertek > jatekos2_ertek:
        print("")
        print("Eredmények:")
        print("")
        print("✅Játékos1 nyert✅")
    elif jatekos1_ertek < jatekos2_ertek:
        print("")
        print("Eredmények:")
        print("")
        print("✅Játékos2 nyert✅")
    elif jatekos1_ertek == jatekos2_ertek:
        print("")
        print("Eredmények:")
        print("")
        print("🕒Döntetlen, játszatok újra🕒")
        
    

if jatekmod == "gép":
     gep_verzio()
elif jatekmod == "ember":
    ember_verzio()
else:
    print("Érvénytelen játékmód.")

