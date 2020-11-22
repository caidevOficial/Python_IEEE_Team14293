import requests

def Pywget(url):
    r = requests.get(url, allow_redirects=True)
    with open(url[url.rfind('/') + 1::], 'wb') as f:
        f.write(r.content)

link = input("Que debo a descargar?: ")
Pywget(link)