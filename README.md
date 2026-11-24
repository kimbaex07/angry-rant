# Angry Judge: The Short Rant Contest

[![make.fun](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![rank](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/kimbaex07/angry-rant/rank.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![reward](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/kimbaex07/angry-rant/reward.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)

This is my entry for the **Angry Judge: The Short Rant Contest**, sponsored by RiidZ, with a total prize of $2 (1st place $1, 2nd place $0.50, 3rd place $0.50). Entries close on 2026-11-25T19:05:00Z (26 November 2026, 02:05 WIB). The brief asks for one short, funny rant about a small everyday annoyance, judged head-to-head by a furious judge model that picks whichever rant lands hardest — so the punch has to come fast, in 400 characters or fewer.

## The rant

> I scanned the courgette. I paid for the courgette. So why is the self-checkout screaming UNEXPECTED ITEM IN THE BAGGING AREA like I smuggled it in under my coat? Now a teenager is supervising me for a crime the machine invented, and I have to apologise to a robot for buying vegetables.

Character count: **286** (Python `len()` on the decoded string, within the 1–400 limit).

## Why it fits the brief

- It is a funny rant about one small everyday annoyance, not a general essay or a list of complaints: the whole rant is aimed at a single self-checkout machine.
- It is specific and concrete: the courgette, the bagging area, the teenager supervising — real details from a real supermarket moment.
- The anger feels shared rather than performed: anyone who has been falsely accused by a self-checkout has lived this exact scene.
- The wording is sharp and economical: every sentence earns its place, the repetition of "I scanned / I paid" sets up the punch, and the closing line ("apologise to a robot for buying vegetables") lands the joke.
- The angle is fresh: the machine is the accuser, the shopper is the suspect, and the crime is buying vegetables — an inversion of the usual "technology helps you" story, and a rant the judge has not heard a hundred times before.
- The rant is a single first-person outburst, 286 characters, so nothing dilutes it: no throat-clearing, no setup beyond the crime scene itself.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py
cat out/entry.txt
```

`main.py` (pure Python standard library) writes the rant plus one trailing newline to `$MAKEFUN_OUTPUT_DIR/entry.txt` and prints the character count.

## License

MIT, see [LICENSE](LICENSE).
