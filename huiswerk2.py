Dag = int( input("welke dag is het vandaag in nummers gezien?"))
if Dag > 7: 
    print("getal is te groot") 
uur = int( input("hoelaat is het momenteel afgerond op hele uren?"))
if uur > 24:
    print("getal is te groot") 

if 1 >= Dag <= 5: 
    if uur > 18:
        print("verwarming moet naar 19 graden") 
    else: 
        print("verwarming moet naar 16 graden")