from bs4 import BeautifulSoup   
import requests,time


# def parsing_barmak():
#     url= "https://barmak.store/category/Acer/"
#     response = requests.get(url=url)
#     soup = BeautifulSoup(response.text, 'lxml')
#     titles = soup.find_all('div', class_ = 'tp-product-tag-2')
#     prices = soup.find_all('span', class_ = 'tp-product-price-2 new-price')
#     # print(titles)
#     # for title in titles:
#     #     print(title.text)
#     # for price in prices:
#     #     print(title.text)
#     with open('laptops.txt', 'w', encoding= 'utf-8') as file:
        
#         for title,price in zip(titles,prices):
#             true_price = "".join(price.text.split ())
#             file.write(f"{title.text}- {true_price} \n ")
    
# parsing_barmak()

def parsing_kurs():
    url="https://www.nbkr.kg/index.jsp?lang=RUS"
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')
    titles = soup.find_all('td', class_ = 'excurr') 
    prices = soup.find_all('td', class_ = 'exrate')
    with open('kursu.txt', 'w', encoding= 'utf-8') as file:
        file.write(time.ctime)
        for title,price in zip(titles,prices):
            true_price = "".join(price.text.split ())
            file.write(f"{title.text}- {true_price}\n ")
parsing_kurs()

