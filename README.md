# The World in One Day — 26 November 2026

[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/news-image-20261126)
[![date](https://img.shields.io/badge/date-26_November_2026-red)](https://make.fun/bounty/news-image-20261126)
[![license](https://img.shields.io/badge/license-MIT-green)](LICENSE)

One image summing up the world's news of **Thursday, 26 November 2026**,
built for the [make.fun bounty](https://make.fun/bounty/news-image-20261126).

## The day in one image

`entry.png` is a one-page newspaper front page: masthead, lead story and
six more stories from the day's wire reports.

- **Lead — Gulf oil under fire:** Yemen's Houthis claim a strike on Ras
  Tanura, Saudi Arabia's largest refinery, as satellite images show thick
  black smoke; Brent crude jumps past $94 a barrel.
- **Gaza:** an Israeli strike kills a Hamas security chief; the ceasefire
  strains.
- **Ukraine:** Kyiv hits two Russian oil refineries; Putin vows retaliation.
- **Trade:** the US plans tariffs of up to 15% on Taiwan; Taipei stocks
  plunge.
- **India:** eighteen years after the Mumbai attacks, India marks
  Constitution Day.
- **Space:** Shenzhou-24 docks at Tiangong with Pakistan's first astronaut,
  Muhammad Zeeshan Ali.
- **Egypt:** a fuel tanker crash sets a Cairo highway ablaze; at least 30 dead.

## How it runs

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png`, or `/output/entry.png` in the grader
sandbox. No network access. The image is 1024×1024 PNG, under 1 MiB,
and both runs write the same bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).

## Sources

Stories as reported on 26 November 2026 by Reuters, AP and AFP via the
day's wire roundups.
