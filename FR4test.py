print("yo waddup")

import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password= "S@v@Bracl3t",
    database="attractiepark_casus_b"
)
cursor = connection.cursor()

query = """
SELECT
    naam,
    werktijd,
    beroepstype,
    bevoegdheid,
    leeftijd,
    specialist_in_attracties,
    pauze_opsplitsen,
    verlaagde_fysieke_belasting
FROM personeelslid
"""

cursor.execute(query)
personeel = cursor.fetchall()

import json
max_fysieke_belasting_json = []

for persoon in personeel:
    naam = persoon[0],
    leeftijd = persoon[4],
    aangepaste_belasting = persoon[7]

if aangepaste_belasting is not None:
    max_fysieke_belasting = aangepaste_belasting
elif leeftijd <= 24:
    max_fysieke_belasting = 25
elif leeftijd <= 50:
    max_fysieke_belasting = 40
else:
    max_fysieke_belasting = 15


max_fysieke_belasting_json.append({
        "naam": naam,
        "leeftijd": leeftijd,
        "verlaagde_fysieke_belasting": aangepaste_belasting,
        "max_fysieke_belasting": max_fysieke_belasting

    }) 

with open("FR4.json", "w", encoding="utf-8") as bestand:
    json.dump(
        {"personeel": max_fysieke_belasting_json},
        bestand,
        indent=4,
        ensure_ascii=False
    )
print("print is klaar cuh")
