import requests
import browser_cookie3
import json

cookies = browser_cookie3.brave(domain_name="osu.ppy.sh")
url = (
    "https://osu.ppy.sh/users/"
    "37147404/extra-pages/top_ranks"
    "?mode=mania"
)

response = requests.get(url, cookies=cookies)

data = response.json()
selected_data = data["best"]["items"][0]

parsed = json.dumps(selected_data)

print(json.dumps(json.loads(parsed), indent=2))
