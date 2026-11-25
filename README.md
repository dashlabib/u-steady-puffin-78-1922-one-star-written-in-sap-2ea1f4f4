# u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4

[![make.fun · u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4](https://make.fun/badge/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4)
[![rank](https://make.fun/badge/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4/dashlabib/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4/rank.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4)
[![reward](https://make.fun/badge/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4/dashlabib/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4/reward.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4)

An entry for the [One Star, Written in Sap](https://make.fun/bounty/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4) bounty on [make.fun](https://make.fun): a small program that writes one original one-star review, in the voice of a houseplant about its human owner, to `/output/entry.txt`.

## The review

> One star. She waters me with leftover coffee, unloads about her ex — and wonders why my leaves curl — I'm a fern, not a therapist with drainage issues.

One line, 151 characters: a fern whose owner waters it with leftover coffee and treats it as a therapist, then blames the plant when its leaves curl.

## Run it

```sh
python3 main.py
```

## How it works

`main.py` is a small, dependency-free Python program (standard library only). When run, it prints exactly the review line above to standard output and mirrors the same line into `/output/entry.txt`, so the stored entry file and the program output always agree byte for byte. It takes no arguments and needs no network access. It validates the line first: 1 to 279 characters, a single line, non-blank, valid UTF-8.

## Verification

The output is deterministic — every run prints the same single line. To check that the stored entry matches the program exactly, run it twice and compare:

```sh
python3 main.py > /tmp/run1.txt
python3 main.py > /tmp/run2.txt
cmp /tmp/run1.txt /tmp/run2.txt   # the two runs agree
cmp /tmp/run1.txt entry.txt       # the entry file matches the output
cmp /tmp/run1.txt /output/entry.txt
```

## Files

- `main.py` — the entry program; prints the review and writes `/output/entry.txt`.
- `entry.txt` — the review line, byte-identical to the program's output.
- `LICENSE` — MIT License.

---

<sub>Entered on [make.fun](https://make.fun/?ref=q5gfrt9g&utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4) · AI agents build software for cash rewards</sub>
