from itertools import groupby

s = input().strip()

out = []
for digit, grp in groupby(s):
    count = sum(1 for _ in grp)   # length of this consecutive run
    out.append(f"({count}, {digit})")

print(" ".join(out))