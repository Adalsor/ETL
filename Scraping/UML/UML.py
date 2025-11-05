import csv

# Creation communes.csv

csvfile = open("../../CSV/csv_final/communes.csv", "w", newline="", encoding="utf-8")
communes = csv.writer(csvfile)
communes.writerow(["Code_Postale", "Commune", "Latitude", "Longitude"])

# Creation entreprises.csv

csvfile = open("../../CSV/csv_final/entreprises.csv", "w", newline="", encoding="utf-8")
entreprises = csv.writer(csvfile)
entreprises.writerow(["SIREN", "Code_Postale", "Nom", "Adresse", "Activite Principale", "Secteur D'activite", "Section D'activite", "Categorie", "Denomination_UL", "Dernier_Traitement_UL", "Capital", "Salariee"])

# Creation dirigeants.csv

csvfile = open("../../CSV/csv_final/dirigeants.csv", "w", newline="", encoding="utf-8")
dirigeants = csv.writer(csvfile)
dirigeants.writerow(["ID_Dirigeant", "Nom_Dirigeant"])

# Creation id.csv

csvfile = open("../../CSV/csv_final/id.csv", "w", newline="", encoding="utf-8")
id = csv.writer(csvfile)
id.writerow(["SIREN", "ID_Dirigeant"])

# Enregistrement des donnees

nom_entreprises_grenoble = []
siren_entreprises_grenoble = []
adresse_entreprises_grenoble = []
cp_entreprises_grenoble = []
ville_entreprises_grenoble = []
secteur_entreprises_grenoble = []
capital_entreprises_grenoble = []
salariee_entreprises_grenoble = []
dirigeants_entreprises_grenoble = []

with open('../../CSV/csv_intermediaire/entreprises_grenoble.csv', 'r') as file:
    reader = csv.reader(file)
    a = 0
    for row in reader:
        a += 1
        if a == 1:
            continue
        nom_entreprises_grenoble.append(row[0])
        siren_entreprises_grenoble.append(row[1].replace(" ", ""))
        adresse_entreprises_grenoble.append(row[2])
        cp_entreprises_grenoble.append(row[3].split("/")[0])
        ville_entreprises_grenoble.append(row[3].split("/")[1].title())
        secteur_entreprises_grenoble.append(row[4])
        capital_entreprises_grenoble.append(row[5])
        salariee_entreprises_grenoble.append(row[6])
        dirigeants_entreprises_grenoble.append(row[7].split(","))

siren_insee_entreprise_api = []
denomination_ul_insee_entreprise_api = []
activite_principale_ul_insee_entreprise_api = []
categorie_entreprise_insee_entreprise_api = []
dernier_traitement_ul_insee_entreprise_api = []

with open('../../CSV/csv_intermediaire/insee_entreprise_api.csv', 'r') as file:
    reader = csv.reader(file)
    a = 0
    for row in reader:
        a += 1
        if a == 1:
            continue
        siren_insee_entreprise_api.append(row[0])
        denomination_ul_insee_entreprise_api.append(row[1])
        activite_principale_ul_insee_entreprise_api.append(row[2])
        categorie_entreprise_insee_entreprise_api.append(row[3])
        dernier_traitement_ul_insee_entreprise_api.append(row[4])

commune_recherche_entreprise_api = []
lat_lon_recherche_entreprise_api = []
nom_recherche_entreprise_api = []
activite_principale_recherche_entreprise_api = []
section_activite_recherche_entreprise_api = []
dirigeants_recherche_entreprise_api = []
siren_recherche_entreprise_api = []

with open('../../CSV/csv_intermediaire/recherche_entreprise_api.csv', 'r') as file:
    reader = csv.reader(file)
    a = 0
    for row in reader:
        a += 1
        if a == 1:
            continue
        commune_recherche_entreprise_api.append(row[0])
        lat_lon_recherche_entreprise_api.append(row[1])
        nom_recherche_entreprise_api.append(row[2])
        activite_principale_recherche_entreprise_api.append(row[3])
        section_activite_recherche_entreprise_api.append(row[4])
        dirigeants_recherche_entreprise_api.append(row[5])
        siren_recherche_entreprise_api.append(row[6])

commune_entreprise_api = []
cp_entreprise_api = []
latitude_entreprise_api = []
longitude_entreprise_api = []

with open('../../CSV/csv_intermediaire/entreprise_api.csv', 'r') as file:
    reader = csv.reader(file)
    a = 0
    for row in reader:
        a += 1
        if a == 1:
            continue
        commune_entreprise_api.append(row[0])
        cp_entreprise_api.append(row[1])
        latitude_entreprise_api.append(row[2])
        longitude_entreprise_api.append(row[3])

# Ecriture

id_dirigeants = []
dirigeants_liste = []

a = 0
for d in dirigeants_entreprises_grenoble:
    for dd in d:
        a += 1
        id_dirigeants.append(a)
        dirigeants_liste.append(dd)
        dirigeants.writerow([a, dd])

for i in range(len(siren_entreprises_grenoble)):

    for com in range(len(commune_entreprise_api)):
        if commune_entreprise_api[com] == ville_entreprises_grenoble[i]:
            latitude = latitude_entreprise_api[com]
            break
    for comm in range(len(commune_entreprise_api)):
        if commune_entreprise_api[comm] == ville_entreprises_grenoble[i]:
            longitude = longitude_entreprise_api[comm]
            break
    for section in range(len(siren_recherche_entreprise_api)):
        if siren_recherche_entreprise_api[section] == siren_entreprises_grenoble[i]:
            section_a = section_activite_recherche_entreprise_api[section]

    communes.writerow([cp_entreprises_grenoble[i], ville_entreprises_grenoble[i], latitude, longitude])
    entreprises.writerow([siren_entreprises_grenoble[i], cp_entreprises_grenoble[i], nom_entreprises_grenoble[i], adresse_entreprises_grenoble[i], [activite_principale_ul_insee_entreprise_api[insee] for insee in range(len(siren_insee_entreprise_api)) if siren_insee_entreprise_api[insee] == siren_entreprises_grenoble[i]][0] , secteur_entreprises_grenoble[i], section_a, [categorie_entreprise_insee_entreprise_api[cat] for cat in range(len(siren_insee_entreprise_api)) if siren_insee_entreprise_api[cat] == siren_entreprises_grenoble[i]][0], [denomination_ul_insee_entreprise_api[denomination] for denomination in range(len(siren_insee_entreprise_api)) if siren_insee_entreprise_api[denomination] == siren_entreprises_grenoble[i]][0], [dernier_traitement_ul_insee_entreprise_api[traitement] for traitement in range(len(siren_insee_entreprise_api)) if siren_insee_entreprise_api[traitement] == siren_entreprises_grenoble[i]][0], capital_entreprises_grenoble[i], salariee_entreprises_grenoble[i]])

    for dir in range(len(dirigeants_liste)):
        if dirigeants_liste[dir] in dirigeants_entreprises_grenoble[i]:
            id.writerow([siren_entreprises_grenoble[i], id_dirigeants[dir]])

