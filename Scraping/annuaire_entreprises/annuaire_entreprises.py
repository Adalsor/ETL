from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import csv

csvfile = open("../../CSV/csv_intermediaire/entreprises_grenoble.csv", "w", newline="", encoding="utf-8")
writer = csv.writer(csvfile)
writer.writerow(["Nom", "SIREN", "Adresse", "CP/Ville", "Secteur", "Capital", "Salarie", "Dirigeants"])

# On initie notre driver et notre lien
driver = webdriver.Chrome()
url = "https://annuaire-entreprises.data.gouv.fr"
driver.get(url)

# On se met à l'endroit que l'on veut
recherche_avancee = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/main/div[1]/form/div[3]/a")))
recherche_avancee.click()
zone_geographique = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/header/div/form/div[2]/div/div/div[1]/div[1]")))
zone_geographique.click()
champ_recherche = driver.find_element(By.XPATH, "/html/body/div[5]/header/div/form/div[2]/div/div/div[1]/div[2]/div[1]/input[1]")
champ_recherche.send_keys("Grenoble")
search_grenoble = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/header/div/form/div[2]/div/div/div[1]/div[2]/div[1]/div/div[2]")))
search_grenoble.click()
appliquer = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/header/div/form/div[2]/div/div/div[1]/div[2]/div[2]/button")))
appliquer.click()

p = 0
while True:
    p += 1
    # On boucle sur les entreprises
    entreprises = driver.find_elements(By.CLASS_NAME, 'style_title__lAmLf')

    for i in range(len(entreprises)):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'style_title__lAmLf')))
        entreprises = driver.find_elements(By.CLASS_NAME, 'style_title__lAmLf')
        entreprises[i].click()

        # Recuperation des info
        try:
            nom_xpath = driver.find_elements(By.XPATH,"/html/body/div[5]/main/div/div[2]/div/div[2]/table/tbody/tr[3]/td[2]/button/span")
            nom = nom_xpath[0].text
        except:
            nom = "/"
        try:
            siren_xpath = driver.find_elements(By.XPATH,"/html/body/div[5]/main/div/div[2]/div/div[2]/table/tbody/tr[4]/td[2]/button/span")
            siren = siren_xpath[0].text
        except:
            siren = "/"
        try:
            adresse_xpath = driver.find_elements(By.XPATH,"/html/body/div[5]/main/div/div[2]/div/div[2]/table/tbody/tr[10]/td[2]/button/span")
            adresse = adresse_xpath[0].text
        except:
            adresse = "/"
        try:
            cp_ville = f"{adresse.split(" ")[-2]}/{adresse.split(" ")[-1]}"
        except:
            cp_ville = "/"
        try:
            secteur_xpath = driver.find_elements(By.XPATH,"/html/body/div[5]/main/div/div[2]/div/div[2]/table/tbody/tr[8]/td[2]/button/span")
            secteur = secteur_xpath[0].text
        except:
            secteur = "/"
        try:
            capital_xpath = driver.find_elements(By.XPATH,"/html/body/div[5]/main/div/div[3]/div[2]/table/tbody/tr[4]/td[2]/button/span")
            capital = capital_xpath[0].text
        except:
            capital = "/"
        try:
            salarie_xpath = driver.find_elements(By.XPATH,"/html/body/div[5]/main/div/div[2]/div/div[2]/table/tbody/tr[12]/td[2]/div/span")
            salarie = salarie_xpath[0].text
        except:
            salarie = "/"

        # Pour la page dirigeants
        dirigeant_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/main/div/div[1]/div[3]/div/a[2]")))
        dirigeant_box.click()
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/main/div/div[2]/div[2]/div/div/div/table')))
            liste_dirigeant_block = driver.find_elements(By.CSS_SELECTOR, "tbody tr")
            dirigeants = []
            a = 0
            for dirigeant in liste_dirigeant_block:
                try:
                    nom_dirigeant = dirigeant.find_element(By.CSS_SELECTOR, "td div span").text.strip().split(", né")[0]
                    if nom_dirigeant != "":
                        a += 1
                        dirigeants.append(nom_dirigeant)
                except:
                    pass
                if a == 3:
                    break
        except:
            dirigeants = ["/"]

        writer.writerow([nom, siren, adresse, cp_ville, secteur, capital, salarie, ", ".join(dirigeants)])

        driver.back()
        driver.back()

    if p == 2:
        break

    # Pagination
    try:
        next_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/main/div/div[2]/div[2]/nav/ul/li[9]/a")))
        next_button.click()

    except TimeoutException:
        print('No more pages')
        break

driver.quit()
