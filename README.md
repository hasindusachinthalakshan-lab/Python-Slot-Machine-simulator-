
# 🎰 Spot — Spin & Bet Machine

A playful, educational command-line slot-machine simulator in Python. Spin reels, place bets, and try your luck — all from the terminal! ⚡

**Quick links**

- Run: `python bet.py`
- Main file: `bet.py`

**Why you'll like it**

- Fun, minimal example to learn Python control flow, randomness, and simple game logic. 🐍
- Zero dependencies — runs anywhere with Python 3.8+. 🚀
- Easy to extend: GUI, persistence, leaderboards, or new game rules. ✨

**Highlights**

- Configurable reels, symbols and payouts (see the top constants in `bet.py`).
- Multi-line betting and per-line wagers.
- Simple console UI — great for beginners and demos.

## Features

- 🎯 Deposit a starting balance and choose how many lines to bet.
- 🎲 Randomized spins with symbol counts defining odds.
- 💰 Payouts calculated from symbol values and bet size.

## Getting started

Prerequisites

- Python 3.8 or newer installed on your system.

Run the game

```bash
python bet.py
```

Gameplay example (sample session)

```
What would you like to deposit?: $20
Current balance is $20
Press enter to spin (q to quit).
Enter the number of lines to bet on (1-3): 3
What would you like to bet on each line? : $2
You are betting $2 on 3 lines. Total bet is: $6

D | C | A
A | A | C
D | D | B

You won $0.
You won on lines:
```

Configuration tips

- Tweak the constants at the top of `bet.py` to change behavior:
  - `max_lines`, `max_bet`, `min_bet` — betting limits.
  - `rows`, `cols` — size of the slot machine grid.
  - `symbols_count` — controls symbol frequency (odds).
  - `symbols_value` — controls payout per symbol.

## Where to get help

- Open an issue in this repository for bugs, questions, or feature ideas. 🐛
- Inspect `bet.py` — the code is intentionally small and readable for quick learning.

## Contributing

- Want to improve the game? Great! Add small, focused PRs and link any changes to an issue.
- See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines (create the file if it doesn't exist). 🙌

## Maintainer

- Maintainer: repository owner (please update this file with contact information). ✉️

## License

See the `LICENSE` file for details.

---

Enjoy spinning! If you'd like, I can add a CONTRIBUTING.md, badges, or a tiny test harness next. 🎉
