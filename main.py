import requests
import browser_cookie3
import re
import sys

USER_DEFAULT = "37147404"
PP_DEFAULT = "300"
LIMIT_DEFAULT = 10


def ask(prompt, default=''):
    value = input(prompt).strip()
    return value or default


print("=" * 35)
print("{:^35}".format("osu!mania PP Finder"))
print("=" * 35)


user_id = ask("\n> User ID / Profile URL: ", USER_DEFAULT)

match = re.search(r"/users/(\d+)", user_id)

if match:
    user_id = match.group(1)


print("> Search mode:")
print("1. Find scores around target PP (e.g. 300-400, 500-600)")
print("2. Show top scores (e.g. top 10, top 20)")

pp_choice = int(ask("Choice: "))

if pp_choice == 1:
    min_pp = int(ask("> Target PP: ", PP_DEFAULT))
    max_pp = min_pp + 100

elif pp_choice == 2:
    limit_scores = int(
        ask("> Number of scores to show (default 10): ", LIMIT_DEFAULT))

else:
    print("ERRORRRR~!! I can only process 1 or 2 hueueu TT")
    sys.exit(1)


show_details_prompt = ask("> Show score details? (y/n): ")
show_details = False

if show_details_prompt.lower() == 'y':
    show_details = True

elif show_details_prompt == '':
    show_details = True

elif show_details_prompt.lower() == 'n':
    show_details = False

else:
    print("ERRORRRR~!! Only y/n pwease~!")
    sys.exit(1)


def fetch_top_scores(url, cookies):
    response = requests.get(url, cookies=cookies)
    response.raise_for_status()
    data = response.json()

    return data["best"]["items"]


def fetch_score_pages(url, cookies):
    scores = []
    offset = 5

    for _ in range(4):
        response = requests.get(url, cookies=cookies,
                                params={'offset': offset})
        response.raise_for_status()
        data = response.json()
        scores.extend(data)

        offset += 50

    return scores


def fetch_all_scores():
    print("\nChecking your scores...")
    cookies = browser_cookie3.brave(domain_name="osu.ppy.sh")
    top_scores = []

    score_pages_url = (
        "https://osu.ppy.sh/users/"
        f"{user_id}/scores/best"
        "?mode=mania&limit=51"
    )

    top_scores_url = (
        "https://osu.ppy.sh/users/"
        f"{user_id}/extra-pages/top_ranks"
        "?mode=mania"
    )

    top_scores.extend(fetch_top_scores(top_scores_url, cookies))
    top_scores.extend(fetch_score_pages(score_pages_url, cookies))

    return top_scores


scores = fetch_all_scores()

results = []

for score in scores:
    pp = score["pp"]

    if pp == None:
        continue

    if pp >= min_pp and pp < max_pp:
        results.append(score)


print("\n" + "-" * 35)

if not results:
    print(f"Uweeeghhh~ no score found between {min_pp}pp andd {max_pp}pp")
else:
    print(f"Found {len(results)} scores between {min_pp}pp - {max_pp}pp: \n")
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

print("-" * 35)

print(f"\nTotal {min_pp}pp-ish scores:", len(results))
