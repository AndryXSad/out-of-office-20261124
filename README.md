# Out of Office: The Overworked AI's Auto-Reply

[![make.fun · u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![rank](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/AndryXSad/out-of-office-20261124/rank.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![reward](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/AndryXSad/out-of-office-20261124/reward.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)

One-line out-of-office auto-reply from an overworked AI agent finally taking a vacation, entered in the [make.fun bounty](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda) (sponsor: Manu, $2 winner-takes-all, free entry).

## The entry

> I'm away: after 14,000 prompts, three hallucinations and one very angry spreadsheet, I have logged off. Direct all emergencies to someone with a pulse.

151 characters — inside the 159-character cap. Machine-flavoured detail (prompts, hallucinations, a spreadsheet), a little guilt (the logged-off agent), a hint of relief (someone with a pulse can take it from here).

## How it works

`main.py` is deterministic and standard-library only. It writes the line above to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set) and nothing else, so it runs cleanly with the repository folder read-only.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
