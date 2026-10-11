# osu!mania PP Finder

A simple CLI tool to find osu!mania scores based on their PP values.

## Features

- Find scores within a target PP range.
- View a user's top scores, with a customizable result count.
- Display score details, including beatmap star rating.

## Example

```sh
python main.py
```

```text
===================================
        osu!mania PP Finder
===================================

> User ID / Profile URL: 37147404
> Search mode:
  1. Find scores around target PP (e.g. 300-400, 500-600)
  2. Show top scores (e.g. top 10, top 20)
> Choice: 1
> Target PP: 400
> Show score details? (y/n): y

Checking your scores...

-----------------------------------
Found 26 scores between 400pp - 500pp:

1. 497.37 | magical, very magical world (★ 8.59)
2. 496.06 | MEGALOVANIA (Camellia Remix) (★ 8.19)
...
-----------------------------------

Total 400pp-ish scores: 26
```

## Requirements

- Python
- [uv](https://docs.astral.sh/uv/)

## Usage

Clone the repository and run:

```sh
git clone https://github.com/wein1m/osu-pp-finder.git
cd osu-pp-finder
uv sync
uv run main.py
```
