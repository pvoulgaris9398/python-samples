import requests
import json

url = "https://api.spaceflightnewsapi.net/v4/articles/38830/?format=json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # Pretty print the JSON to see the nested structure
    # print(json.dumps(data, indent=4))


    # authors = [x.get("name") for x in data.get("authors", {})]
    authors = [x for x in data.get("authors", {})]

    print("Authors:")
    print(json.dumps(authors, indent=4))

    authors = [(x.get("name"), x.get("socials", {})) for x in data.get("authors", {})]
    
    print("Authors:")
    print(json.dumps(authors, indent=4))

else:
    print(f"Failed to retrieve data: {response.status_code}")
