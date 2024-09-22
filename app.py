from googlesearch import search
from flask import Flask, redirect

app = Flask(__name__)

def get_url_from_file():
    # data.txt dosyasını aç ve ilk satırdaki kelimeyi al
    with open('data.txt', 'r') as file:
        query = file.readline().strip()
    return query

def search_google(query):
    # Google'da arama yap ve ilk sonucun başlığını al
    search_results = search(query, num_results=1)
    
    for result in search_results:
        return result  # İlk sonucu döndür

    return None

@app.route('/')
def home():
    # data.txt dosyasından kelime alalım
    initial_query = get_url_from_file()
    
    # İlk Google araması ve başlıkla beraber URL'yi alalım
    first_result_url = search_google(initial_query)
    
    if first_result_url:
        # "izle" kelimesiyle tekrar arama yapalım
        new_query = f"{initial_query} izle"
        final_result_url = search_google(new_query)
        
        if final_result_url:
            return redirect(final_result_url)  # Kullanıcıyı ilk çıkan sonuca yönlendir
        else:
            return "No search results found after 'izle' query."
    else:
        return "No search results found for the initial query."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
