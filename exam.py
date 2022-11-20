import requests
from bs4 import BeautifulSoup
import lxml
import fake_useragent

class Parser():
    def __init__(self):
        self.user = fake_useragent.UserAgent().random
        self.headers = {'user-agent': self.user}
        self.session = requests.Session()
        self.page = int(input('Input page '))

    def a(self):

        for j in range(1, self.page+1):
            url = f'https://hard.rozetka.com.ua/ua/monitors/c80089/page={j}'
            response = self.session.get(url, headers=self.headers)
            soup = BeautifulSoup(response.text, "lxml")


#https://hard.rozetka.com.ua/ua/monitors/c80089/



            all_product = soup.find('ul', class_='catalog-grid ng-star-inserted')
    # print(all_product)
            product_list = all_product.find_all('li', class_='catalog-grid__cell catalog-grid__cell_type_slim ng-star-inserted')
    # print(product_list)

            for i in range(len(product_list)):
                product = product_list[i].find('a', class_='goods-tile__heading ng-star-inserted').text
                try:
                    new_price = product_list[i].find('span', class_='goods-tile__price-value').text.replace(' ',' ')
                    with open('myproduct.txt', 'a', encoding='UTF-8') as file:
                        file.write(f"{product}  New price {new_price}'\n'")
                except AttributeError:
                    print('New price no!')
            print(f"Закончил {j} страницу")

pars = Parser()
print(pars.a())