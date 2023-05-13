# fetch images from google.com

from bs4 import BeautifulSoup
import urllib.request

import os
from filter import filter


def readfile(filepath):
    with open(filepath,'r',encoding='utf-8') as file:
        content = file.read()
    return content

def fetch_data(content_class, save_to_file = "images.txt"):
    # print(f"[+] fetching {url}...")

    # page = requests.get(url)
    page = readfile('page.html')

    tags = BeautifulSoup(page, 'html.parser').find_all(class_ = content_class)
    eyewares = [data['src'] for data in tags if 'src' in data.attrs]

    # saving data
    with open(save_to_file, 'a', encoding='utf-8') as file:
        file.write("\n".join(eyewares))

def download_image(url, fname):
    urllib.request.urlretrieve(url, fname)

# download all the images
def download():
    # filter the data and save it to filtered
    if not os.path.exists('filtered'):
        os.makedirs('filtered')

    links = list(set(readfile('images.txt').split('\n')[2000:]))
    i = 1000
    j = 0 
    while True:
        print(i, j)
        try:
            download_image(links[j], "temp.jpg")
            if filter('temp.jpg', f"filtered/{i}"):
                i += 1
            j += 1 
        except Exception as e:
            print('[error]', str(e))
            break

    print('total=',len(links))
    print('filtered=',len(os.listdir('filtered')))

    # for i in os.listdir('data'):
    #     print(f"data/{i}")
    #     filter(f"data/{i}", f"filtered/{i}")



# fetch_data(content_class="rg_i Q4LuWd")

download()






