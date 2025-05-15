import random
print("Ez a 21-es kártyajáték")
jatekmod = input("Gép vagy ember ellen szeretnél játszani?")
if jatekmod == "gép":
    print("gép lapjai:")
gep_kartya = []
gep_kartya.append(4)
gep_kartya.append(5)
print(gep_kartya)
gep_lap_ertek = sum(gep_kartya)
print(f"Össesen:{gep_lap_ertek}")

print("jatekos lapjai:")
jatekos_kartya = []
jatekos_kartya.append(random.randint(2,11))
jatekos_kartya.append(random.randint(2,11))
print(jatekos_kartya)
jatekos_kartya_ertek = sum(jatekos_kartya)
print(f"Összesen:{jatekos_kartya_ertek}")