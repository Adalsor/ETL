import requests
import csv
import time
from unidecode import unidecode

liste_nom_communne = []
with open(r'/1er-Depot/Scraping/annuaire_entreprises\entreprises_grenoble.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        liste_nom_communne.append(row[3].split('/')[1].title())
for commune in liste_nom_communne:
    if commune == 'Â–ªï¸Ž' or commune == "Ville":
        liste_nom_communne.remove(commune)

csvfile = open("../../CSV/csv_intermediaire/entreprise_api.csv", "w", newline="", encoding="utf-8")
writer = csv.writer(csvfile)
writer.writerow(["Nom de la Commune", "Code Postale", "Latitude", "Longitude"])

url = "https://geo.api.gouv.fr/communes"
parametres_api = {'fields': 'nom,codesPostaux,centre'}
r = requests.get(url, params = parametres_api)
contenu = r.json()

for commune in liste_nom_communne:
    cp = []
    for i in contenu:
        if unidecode(i['nom'].title()) == commune:
            cp += i['codesPostaux']
            latitude = i['centre']['coordinates'][1]
            longitude = i['centre']['coordinates'][0]
    writer.writerow([commune, cp, latitude, longitude])
