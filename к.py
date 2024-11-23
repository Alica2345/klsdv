import requests
from bs4 import BeautifulSoup


class SiteManager:
    def __init__(self):

        self.sites = [
            "https://www.netflix.com/browse",
            "https://rozetka.com.ua/ua/"
        ]

    def add_site(self, site):
        if site not in self.sites:
            self.sites.append(site)
            print(f"Сайт {site} добавлен.")
        else:
            print(f"Сайт {site} уже существует.")

    def get_sites(self):
        return self.sites


class SiteParser:
    def search_on_site(self, site, query):
        try:
            response = requests.get(site)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            content = soup.get_text().lower()
            return content.count(query.lower())
        except Exception as e:
            print(f"Ошибка при обработке сайта {site}: {e}")
            return 0



class UserInterface:
    def show_menu(self):
        print("Меню:")
        print("1 Додати сайт")
        print("2 Показать сайты")
        print("3 Шукати на сайтах")
        print("4 Виход")
        return input("Выберите действие: ")

    def get_input(self, prompt):
        return input(prompt)

    def show_message(self, message):
        print(message)


class SearchApp:
    def __init__(self):
        self.site_manager = SiteManager()
        self.site_parser = SiteParser()
        self.ui = UserInterface()

    def run(self):
        while True:
            choice = self.ui.show_menu()
            if choice == "1":
                site = self.ui.get_input("Введите URL сайта: ")
                self.site_manager.add_site(site)
            elif choice == "2":
                sites = self.site_manager.get_sites()
                if sites:
                    self.ui.show_message("Добавленные сайты:")
                    for site in sites:
                        print(site)
                else:
                    self.ui.show_message("Список сайтов пуст.")
            elif choice == "3":
                query = self.ui.get_input("Введите поисковый запрос: ")
                results = {}
                for site in self.site_manager.get_sites():
                    count = self.site_parser.search_on_site(site, query)
                    results[site] = count
                sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
                self.ui.show_message("Результаты поиска:")
                for site, count in sorted_results:
                    print(f"{site}: {count} совпадений")
            elif choice == "4":
                self.ui.show_message("Выход из программы.")
                break
            else:
                self.ui.show_message("Некорректный ввод, попробуйте снова.")


if __name__ == "__main__":
    app = SearchApp()
    app.run()