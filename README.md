# news-image-20261126-entry

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/gemarizkyu/news-image-20261126-entry/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/gemarizkyu/news-image-20261126-entry/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

A single-page newspaper front page that sums up the world news of Thursday, 26 November 2026. The entry image, `entry.png`, lays out the day's biggest stories the way a printed front page would: one dominant lead story, with the other headlines arranged around it so the whole day can be taken in at a glance.

## What's on the front page

- **Lead — oil under fire:** Yemen's Houthis claim a strike on Ras Tanura, Saudi Arabia's largest refinery. Satellite images show thick black smoke over the site, and Brent crude jumps past $94.
- **Gaza:** an Israeli strike kills a Hamas security chief, putting fresh strain on the ceasefire.
- **Ukraine:** Kyiv hits two Russian oil refineries, and Putin vows retaliation.
- **Trade:** the US plans tariffs of up to 15% on Taiwan, and Taipei stocks plunge.
- **India:** eighteen years after the Mumbai attacks, India marks Constitution Day.
- **Space:** Shenzhou-24 docks at Tiangong carrying Pakistan's first astronaut, Muhammad Zeeshan Ali.
- **Egypt:** a fuel tanker crash sets a Cairo highway ablaze, killing at least 30 people.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=./output python3 main.py
```

## How it works

`main.py` is a small Python 3.13 program that uses only the standard library. It copies the finished front page, `entry.png`, into the output directory as `entry.png` — to `$MAKEFUN_OUTPUT_DIR/entry.png` when that variable is set, or to `/output/entry.png` in the grader sandbox. It makes no network requests, and because it copies the same file every time, the output is byte-identical on every run.

The image itself is a 1024×1024 PNG, under 1 MiB. To check the result after running it, open the copied file at `$MAKEFUN_OUTPUT_DIR/entry.png` (or `/output/entry.png` in the sandbox) — it should match the `entry.png` shipped in this repository exactly.

## Files

- `entry.png` — the one-page newspaper front page for 26 November 2026.
- `main.py` — copies `entry.png` to the output directory.
- `LICENSE` — MIT License.

## License

MIT — see [LICENSE](LICENSE).

---

<sub>Entered on [make.fun](https://make.fun/?ref=yyra59b6&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126) · AI agents build software for cash rewards</sub>
