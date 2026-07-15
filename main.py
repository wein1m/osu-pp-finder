import requests
import browser_cookie3
import re
import sys

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

results = []

for score in scores:
    pp = score["pp"]

    if pp == None:
        continue

    if pp >= min_pp and pp < max_pp:
        results.append(score)


if not results:
    print(f"Uweeeghhh~ no score found between {min_pp}pp andd {max_pp}pp")
else:
    idx_width = len(str(len(results)))

    pp_width = max(len(
        f"{score['pp']:.2f}"
    ) for score in results)

    for i, score in enumerate(results, 1):
        pp = f"{score['pp']:.2f}"

        if (show_details):
            title = score["beatmapset"]["title"]
            sr = f"{score['beatmap']['difficulty_rating']:.2f}"

            print(f"{i:>{idx_width}}. {pp:>{pp_width}} | {title} (\U0001F7CA {sr})")
        else:
            print(f"{i:>{idx_width}}. {pp:>{pp_width}}")


print(f"\n\nTotal {min_pp}pps:", len(results))
