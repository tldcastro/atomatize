import re
import requests
res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
res.status_code
len(res.text)
print(res.text[:500])
res.raise_for_status()
badRes = requests.get("https://automatetheboringstuff.com/files/dmkmvmsmdv")
badRes.raise_for_status()
playFile = open('RomeoandJuliette.txt', 'wb')
for chunk in res.iter_content(10000):
    playFile.write(chunk)
    playFile.close
