import datetime
from pathlib import Path

COUNTER_FILE = Path(__file__).parent / "counter.txt"


def read_current_count() -> int:
    if not COUNTER_FILE.exists():
        return 0
    text = COUNTER_FILE.read_text().strip()
    if not text:
        return 0
    value = text.split(" - ")[0]
    try:
        return int(value)
    except ValueError:
        return 0


def main() -> None:
    new_count = read_current_count() + 1
    timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    COUNTER_FILE.write_text(f"{new_count} - {timestamp}\n")
    print(f"Counter updated to {new_count} at {timestamp}")


if __name__ == "__main__":
    main()
