straat = input("In welke straat woon je? ")
huisnummer = input("Wat is het huisnummer? ")
plaats = input("In welke plaats is dat? ")
postcode = input("wat is je postcode cuh?")

# Toon het adres
print("dan is je adres dus")
print(f"{straat} {huisnummer}") 
print(f"in {plaats}") 
print(f"met de postcode {postcode}")




aantal = int(input("Geef aantal vogels"))
if aantal <= 1:
    print(f"ik zie {aantal} vogel")
else:
    print(f"ik zie {aantal} vogels")

print("type ik, jij of hij\n")
persoon = input("type ik, jij of hij")
verjaardag = "16 april"

print (persoon)

if persoon == "ik":
    print(f"ik ben jarig op {verjaardag}") 
else:
    if persoon == "jij":
        print(f"jij bent jarig op {verjaardag}")
    else:
        print(f"hij is jarig op {verjaardag}")


print("type ik, jij of hij\n")
persona = input("type ik, jij of hij")
jaardag = "16 april"

print(persona, end="") 

if persona == "jij":
    print("bent", end="")
elif persona == "ik":
    print("ben", end="")
else:
    print("is", end="")

print(f"jarig op{verjaardag}")



print("Hoe oud ben je?")
leeftijd = int(input())
if leeftijd < 18:
    print("je mag niet stemmen cuh") 
else:
    print (f"Je bent {leeftijd}, dus je mag stemmen cuh")