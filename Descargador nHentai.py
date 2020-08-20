#! python3

import requests, os, bs4

print('Type the Atomic Number:')
atomicNum = input()
foldername = 'nHentai_' + atomicNum

os.makedirs(foldername, exist_ok=True)

url = 'https://nhentai.net/g/' + atomicNum

res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'lxml')  # lxml es la alternativa a html.paser

sig = soup.select('#thumbnail-container > div > div > a')  #css selector para esta ocasion.
for i in range(len(sig)):
    salsa = sig[i].get('href')
    print('Downloading: page ' + str(i) + '...')
    link = 'https://nhentai.net' + salsa
    res = requests.get(link)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    pag = soup.select('#image-container > a > img')
    donw = pag[0].get('src')
    res = requests.get(donw)
    imageFile = open(os.path.join(foldername, os.path.basename(donw)),'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

print('Donwload Complete!')
print('Hentai saved in: ' + foldername)
