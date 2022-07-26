# abrindo um endereço no google maps via terminal

import webbrowser
import pyperclip
import sys
import requests

map_websites_base_url = {
    'google-maps': "https://www.google.com/maps/search/",
    'uol': 'https://busca.uol.com.br/result.html?term=',
}

# python cap-11/mapit.py google-maps asdas
# python cap-11/mapit.py uol asdas
# python 11/mapit.py

if len(sys.argv) > 1:
    website_key = "".join(sys.argv[1])
    term = "".join(sys.argv[2:])
elif len(sys.argv) <= 1:
    website_key = input("Chave do site de busca (google-maps, uol): ")
    term = input("Digite termo busca: ")
else:
    term = pyperclip.paste()
url = map_websites_base_url[website_key] + term
webbrowser.open(url)
#res = requests.get(url)
# print(res.text)
