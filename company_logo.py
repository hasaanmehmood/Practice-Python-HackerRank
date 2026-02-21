from collections import Counter

s = input().strip()
freq = Counter(s)

top3 = sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:3]

for ch, count in top3:
    print(ch, count)