import requests
from pathlib import Path
import os
import json

def downloadCardImages(baseDir, jsonData, cmc, sortByCMC=True):
    directory = f"{baseDir}/{cmc}" if sortByCMC else f"{baseDir}"
    Path(directory).mkdir(parents=True, exist_ok=True)
    ListOfExistingFiles = os.listdir(directory)
    while True:
        ListOfCheckedCards = [os.path.splitext(file)[0] for file in ListOfExistingFiles]
        for card in jsonData["data"]:
            if card['name'] not in ListOfCheckedCards:
                try:
                    url = card["image_uris"]["large"]
                    name = f"{card['name'].replace('/', '|')}"
                    img_data = requests.get(url).content
                    with open(f"{directory}/{name}.jpg", 'wb') as image:
                        image.write(img_data)
                        print(f"downloaded {directory}/{name}.jpg")
                except KeyError:
                    print(f"{card['name']} has no image_uri")
        if jsonData['has_more']:
            response = requests.get(jsonData["next_page"])
            jsonData = json.loads(response.content)
        else:
            break


os.chdir(Path(__file__).parent.resolve())
listOfCMCs = []
listOfResponse = []
for cmc in range(0,30):
    response =  requests.get(f"https://api.scryfall.com/cards/search?q=t%3Acreature+mv%3D{cmc}")
    json_response = json.loads(response.content)
    if response.status_code == 200:
        downloadCardImages("creatures", json_response, cmc)
    response =  requests.get(f"https://api.scryfall.com/cards/search?q=t%3Aequipment+mv%3D{cmc}")
    json_response = json.loads(response.content)
    if response.status_code == 200:
        downloadCardImages("equipment", json_response, cmc)
    response =  requests.get(f"https://api.scryfall.com/cards/search?q=t%3Ainstant+mv%3D{cmc}")
    json_response = json.loads(response.content)
    if response.status_code == 200:
        downloadCardImages("instants", json_response, cmc, False)
    response =  requests.get(f"https://api.scryfall.com/cards/search?q=t%3Asorcery+mv%3D{cmc}")
    json_response = json.loads(response.content)
    if response.status_code == 200:
        downloadCardImages("sorceries", json_response, cmc, False)
    
        