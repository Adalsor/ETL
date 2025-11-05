import requests
import csv

# Creation CSV

csvfile = open("../../CSV/csv_intermediaire/insee_entreprise_api.csv", "w", newline="", encoding="utf-8")
writer = csv.writer(csvfile)
writer.writerow(["Siren", "Denominaton UL", "Activite Principale UL", "Categorie Entreprise", "Dernier Traitement UL"])

# Creation de siren_list

siren_liste = []
with open(r'/1er-Depot/Scraping/annuaire_entreprises\entreprises_grenoble.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        siren_liste.append(row[1].replace(" ", ""))
siren_liste = siren_liste[1:]

# Parametrages

base_url = "https://api.insee.fr/api-sirene/3.11/siren/"
for siren in siren_liste:
    url = base_url + siren
    header = {'X-INSEE-Api-Key-Integration': 'a1e47f92-745d-496d-a47f-92745d396dcf'}
    r = requests.get(url, headers=header)
    data = r.json()

    # Enregistrement CSV

    writer.writerow([data['uniteLegale']["siren"], data['uniteLegale']["periodesUniteLegale"][0]["denominationUniteLegale"], data['uniteLegale']["periodesUniteLegale"][0]["activitePrincipaleUniteLegale"], data['uniteLegale']["categorieEntreprise"], data['uniteLegale']["dateDernierTraitementUniteLegale"]])
