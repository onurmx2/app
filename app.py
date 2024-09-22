import requests
from bs4 import BeautifulSoup
from flask import Flask

app = Flask(__name__)

def get_url_from_file():
    # data.txt dosyasını aç ve ilk satırdaki URL'yi al
    with open('data.txt', 'r') as file:
        url = file.readline().strip()
    return url

def search_google(query):
    # Google'da arama yapmak için URL oluştur
    query = query.replace(' ', '+')
    url = f'https://www.google.com/search?q={query}'
    
    # Google sayfasını çek
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)

    # HTML içeriğini BeautifulSoup ile işleyelim
    soup = BeautifulSoup(response.text, 'html.parser')

    # İlk sonucu bulmak için HTML yapısında gezinelim (Google bazen sonuç yapısını değiştirir)
    search_results = soup.find_all('a', href=True)
    for result in search_results:
        link = result['href']
        if "url?q=" in link:  # Google arama sonuç linkleri "url?q=" ile başlar
            return link.split("url?q=")[1].split("&")[0]

    return None

@app.route('/')
def home():
    # data.txt dosyasından URL alalım
    url_from_file = get_url_from_file()
    
    # Google'da bu URL'yi ara ve ilk sonuca git
    first_result_url = search_google(url_from_file)
    
    if first_result_url:
        return f"First search result: <a href='{first_result_url}'>{first_result_url}</a>"
    else:
        return "No search results found."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
