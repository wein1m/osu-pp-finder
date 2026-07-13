import requests
import browser_cookie3
import json

user_id = input("Input User ID: ") or "37147404"


def get_top_scores():
    cookies = browser_cookie3.brave(domain_name="osu.ppy.sh")

    url = (
        "https://osu.ppy.sh/users/"
        f"{user_id}/scores/best"
        "?mode=mania&limit=200"
    )

    response = requests.get(url, cookies=cookies)

    return response.json()


scores = get_top_scores()

count = 0

for score in scores:
    pp = score["pp"]
    if pp >= 300 and pp < 400:
        count += 1
        print(f"{count}. {pp}")

print("\n\nTotal 300s:", count)
