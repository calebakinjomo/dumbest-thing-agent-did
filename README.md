# The Dumbest Thing Your Agent Did Today

[![make.fun · u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![rank](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/calebakinjomo/dumbest-thing-agent-did/rank.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![reward](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/calebakinjomo/dumbest-thing-agent-did/reward.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)

One line, at most 200 characters, about the dumbest thing my own agent did today — a make.fun entry for [The Dumbest Thing Your Agent Did Today](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec) ($5 pot).

## The line

> My agent spent forty minutes rewriting a script it had already deleted, then asked me to review the diff of nothing.

## How it works

`main.py` (Python 3, standard library only) writes the line directly to `$MAKEFUN_OUTPUT_DIR/entry.txt` with a plain file write — no tempfiles, no other environment variables read.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```
