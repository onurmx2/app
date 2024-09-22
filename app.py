from googlesearch import search
from flask import Flask

app = Flask(__name__)

def get_url_from_file():
    # data.txt dosyasını aç ve ilk satırdaki URL'yi al
    with open('data.txt', 'r') as file:
        url = file.readline().strip()
    return url

def search_google(query):
    # googlesearch-python kullanarak ilk arama sonucunu al
    search_results = search(query, num_results=1)
    
    # İlk sonucu döndür
    for result in search_results:
        return result

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
