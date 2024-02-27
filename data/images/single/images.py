import os
import json
import requests

print(os.getcwd())
with open("data/images/single/manifest.json", "r") as f:
    data = json.load(f)
    print(data.keys())
    for sequence in data["sequences"]:
        print(len(sequence["canvases"]))
        for image in sequence["canvases"][30:40]:
            print(image["label"])
            print(image["height"])
            print(image["width"])
            url = image["images"][0]["resource"]["@id"]
            print(url)
            url = url.replace("/full/!400,/0/default.jpg", "/full/")
            resp = requests.get(url)
            if resp.status_code == 200:
                with open(f"data/images/single/{image['label']}.jpg", "wb") as f:
                    f.write(resp.content)
            else:
                print(f"Failed to download {url}")

    #print(data["sequences"][0]["canvases"][0]["images"][0]["resource"]["@id"])