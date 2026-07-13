import requests
import browser_cookie3
import re
import sys
import json

USER_DEFAULT = "37147404"
PP_DEFAULT = "300"


def ask(prompt, default=''):
    value = input(prompt).strip()
    return value or default


user_id = ask("Input User ID: ", USER_DEFAULT)

match = re.search(r"/users/(\d+)", user_id)

if match:
    user_id = match.group(1)


min_pp = int(ask("Input Wanted PP: ", PP_DEFAULT))
max_pp = min_pp + 100


show_details_prompt = ask("Show Details (y/n): ")
show_details = False

if show_details_prompt.lower() == 'y':
    show_details = True

elif show_details_prompt == '':
    show_details = True

elif show_details_prompt.lower() == 'n':
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
    title = score["beatmapset"]["title"]
    sr = round(score["beatmap"]["difficulty_rating"], 2)

    if pp >= min_pp and pp < max_pp:
        # print(json.dumps(score, indent=2))
        count += 1
        if (show_details):
            print(f"{count}. {pp} | {title} (\U0001F7CA {sr})")
        else:
            print(f"{count}. {pp}")


print(f"\n\nTotal {min_pp}pps:", count)
