import re

def find_start_end(s: str, sub: str):
    # (?=...) is a lookahead that allows overlapping matches
    matches = list(re.finditer(rf'(?={re.escape(sub)})', s))
    if not matches:
        print((-1, -1))
        return

    for m in matches:
        start = m.start()
        end = start + len(sub) - 1  # HackerRank wants inclusive end.
        print((start, end))


# Example
if __name__ == "__main__":
    s = "aaadaa"
    sub = "aa"#
    find_start_end(s, sub)
    # (0, 1)
    # (1, 2)
    # (4, 5)