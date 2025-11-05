import requests
import csv
import time

# Liste commune/lat/lon

commune_temp = []
latitude_temp = []
longitude_temp = []
commune = []
latitude = []
longitude = []
with open(r'/1er-Depot/Scraping/API/entreprise_api.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        commune_temp.append(row[0])
        latitude_temp.append(row[2])
        longitude_temp.append(row[3])

for i in range(len(commune_temp)):
    if commune_temp[i] not in commune:
        commune.append(commune_temp[i])
        latitude.append(latitude_temp[i])
        longitude.append(longitude_temp[i])

commune.pop(0)
latitude.pop(0)
longitude.pop(0)

# Parametrages
url = "https://recherche-entreprises.api.gouv.fr/near_point"
liste = ['nom_raison_sociale', 'activite_principale', 'section_activite_principale' ,'dirigeants', 'siren']
csvfile = open("../../CSV/csv_intermediaire/recherche_entreprise_api.csv", "w", newline="", encoding="utf-8")
writer = csv.writer(csvfile)
writer.writerow(["Commune aux 10Km", "Lat/Lon", "Nom Entreprise", "Activite Principale", "Section d'activite", "Dirigeants", "Siren"])
for c in range(len(commune)):
    time.sleep(1)
    parametres = {'lat': latitude[c], 'long': longitude[c], 'radius': 1, 'fields': 'activite_principale,section_activite_principale'}
    r = requests.get(url, params=parametres)
    data = r.json()

    for d in data['results']:
        writer.writerow([commune[c], [latitude[c], longitude[c]], d['nom_raison_sociale'], d['activite_principale'], d['section_activite_principale'], d['dirigeants'], d['siren']])

