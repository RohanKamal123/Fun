# Auto Commit Counter

A GitHub Actions workflow that runs twice a day, bumps a counter, and commits the result back to the repo.

## How it works

1. `.github/workflows/counter.yml` fires on a schedule (`0 0,12 * * *`, i.e. 00:00 and 12:00 UTC) or manually via `workflow_dispatch`.
2. It checks out the repo and runs `counter.py`.
3. `counter.py` reads the current value from `counter.txt`, increments it, and writes back `<count> - <UTC timestamp>`.
4. The workflow commits and pushes `counter.txt` if it changed.

## Running it manually

```bash
python counter.py
```

## Changing the schedule

Edit the `cron` expression in `.github/workflows/counter.yml`. GitHub Actions schedules are UTC and can be delayed under load, so treat the times as approximate.
