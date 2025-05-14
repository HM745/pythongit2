import random
print("Ez a 21-es kártyajáték")
print("gep lapjai:")
geplap1 = random.randint(2,11)
print(geplap1)
geplap2 = random.randint(2,11)
print(geplap2)
print("jatekos lapjai:")
jatekos1_lap1 = random.randint(2,11)
print(jatekos1_lap1)
jatekos1_lap2 = random.randint(2,11)
print(jatekos1_lap2)

gep_osszesitett_ertek = geplap1 + geplap2
print("Összesített érték:",gep_osszesitett_ertek)

jatekos1_osszesitett_ertek = jatekos1_lap1 + jatekos1_lap2
print("Összesített érték:",jatekos1_osszesitett_ertek)

