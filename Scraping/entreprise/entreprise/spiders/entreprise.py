import scrapy


class EntrepriseSpider(scrapy.Spider):
    name = "entreprise"
    allowed_domains = ["www.societe.com"]
    start_urls = ["https://www.societe.com/entreprises/isere-38"]

    def parse(self, response):
        select_html = response.xpath("/html/body/main/div[2]")

        for lien in select_html.css("li"):
            numero = lien.css("a span::text").get()
            if numero == "62" or numero == "63":
                pages = lien.css("a::attr(href)").get()
                yield response.follow(pages, callback=self.parse2)

    def parse2(self, response):
        select_html = response.xpath("/html/body/main/div[2]")
        for lien in select_html.css("li"):
            pages = lien.css("a::attr(href)").get()
            yield response.follow(pages, callback=self.parse3)

    def parse3(self, response):
        select_html = response.xpath("/html/body/main/div[2]")
        for lien in select_html.css("li"):
            yield {
                "Nom": lien.css("p span.ui-a::text").get(),
                "Localisation": lien.css("p span.dpt-address::text").get(),
                "Siren": lien.css("p span.xDpID::text").get()
            }

# Pour lancer le fichier:
# scrapy crawl entreprise -O entreprise.csv

# Avec Chat pour separer en plusieurs colonnes:
# scrapy crawl entreprise -O entreprise.csv -s FEED_EXPORT_FIELDS='Nom,Localisation,Siren' -s FEED_EXPORT_ENCODING=utf-8 -s CSV_DELIMITER=';'

