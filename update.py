import requests
from pathlib import Path
import os
import json

os.chdir(Path(__file__).parent.resolve())
listOfCMCs = []
listOfResponse = []
for cmc in range(0,30):
    response =  requests.get(f"https://api.scryfall.com/cards/search?q=t%3Acreature+mv%3D{cmc}")

    if response.status_code == 200:
        Path(f"creatures/{cmc}").mkdir(parents=True, exist_ok=True)
        listOfCMCs.append(cmc) 
        json_response = json.loads(response.content)
        for cards in json_response["data"]:
            try:
                url = cards["image_uris"]["png"]
                name = f"{cards['name'].replace('/', '|')}"
                img_data = requests.get(url).content
                with open(f"creatures/{cmc}/{name}.png", 'wb') as image:
                    image.write(img_data)
            except KeyError:
                print(f"{cards['name']} has no image_uri")
        pass