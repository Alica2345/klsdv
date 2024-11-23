import requests
from bs4 import BeautifulSoup
url = "https://www.marvel.com"
another_url = "https://www.dc.com"
class SiteManager:
    def init(self):
        self.sites = []

    def add_site(self, url):
        self.sites.append(url)

    def get_sites(self):
        return self.sites

class SiteParser:
    def searchonsite(self, url, aboba):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            page_text = soup.get_text().lower()
            query_lower = aboba.lower()
            return page_text.count(query_lower)
        except requests.exceptions.RequestException:
            print(f"Ошибка при доступе к сайту: {url}")
            return 0


class SearchApp:
    def init(self):
        self.site_manager = SiteManager()
        self.site_parser = SiteParser()

    def run(self):
        while True:
            print("\n1. Додати сайт")
            print("2. Пошук на сайтах")
            print("3. Переглянути сайт")
            print("4. Вихід")
            choice = input("Виберіть варіант: ")

            if choice == "1":
                url = input("Введіть URL сайту для додавання: ")
                self.site_manager.add_site(url)
                print(f"Сайт {url} додано")
            elif choice == "2":
                aboba = input("Введіть пошуковий запит: ")
                sites = self.site_manager.get_sites()

                results = []
                for site in sites:
                    matches = self.site_parser.searchonsite(site, aboba)
                    if matches > 0:
                        results.append((site, matches))
                print("\nРезультати пошуку:")
                for site, matches in results:
                    print(f"{site} - {matches} совподає")
            elif choice == "3":
                print("Сайти є:")
                for site in self.site_manager.get_sites():
                    print(site)

            elif choice == "4":
                print("Вийти з програми")
                return 0
            else:
                print("Некорректный выбор. Try again")
app = SearchApp()
app.run()