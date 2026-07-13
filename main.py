import requests
import browser_cookie3
import re
import sys

user_id = input("Input User ID: ") or "37147404"

match = re.search(r"/users/(\d+)", user_id)

if match:
    user_id = match.group(1)


min_pp = input("Input Wanted PP: ") or "300"

min_pp = int(min_pp)

max_pp = min_pp + 100


show_details_prompt = input("Show Details (y/n): ")
show_details = False

if show_details_prompt.lower().strip() == 'y':
    show_details = True
elif show_details_prompt.lower().strip() == 'n':
    show_details = False
elif show_details_prompt.strip() == '':
    show_details = False
else:
    print("Only y/n pwease~!")
    sys.exit(1)


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
    if pp >= min_pp and pp < max_pp:
        count += 1
        print(f"{count}. {pp}")

print(f"\n\nTotal {min_pp}pps:", count)
