# fetching data from lenskart

from modules import *

# lenskart_url = "https://www.lenskart.com/eyeglasses.html"

def fetch_data(content_class, save_to_file = "eyewares-from-lenskart.txt"):
    # print(f"[+] fetching {url}...")
    print("[+] Scraping eyewares links")

    # page = requests.get(url)
    with open('lenskart.html', encoding='utf-8') as file:
        page = file.read()

    tags = BeautifulSoup(page, 'html.parser').find_all(class_ = content_class)
    eyewares = [data['src'] for data in tags if 'src' in data.attrs]

    # saving data
    with open(save_to_file, 'w', encoding='utf-8') as file:
        file.write("\n".join(eyewares))

fetch_data(content_class = "getGaData sliderImg")

