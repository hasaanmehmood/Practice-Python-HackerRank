# A newly opened multinational brand has decided to base their company logo on the three most common characters in 
# the company name. They are now trying out various combinations of company names and logos based on this condition. 
# Given a string , which is the company name in lowercase letters, your task is to find the top three most common 
# characters in the string. Print the three most common characters along with their occurrence count. Sort in 
# descending order of occurrence count. If the occurrence count is the same, sort the characters in alphabetical 
# order. For example, according to the conditions described above, would have it's logo with the letters . Input
# Format A single line of input containing the string . Constraints 3<=len(S)<=10^4 S has at least 3 distinct characters 
# Output Format Print the three most common characters along with their occurrence count each on a separate line. Sort 
# output in descending order of occurrence count. If the occurrence count is the same, sort the characters in 
# alphabetical order..


from collections import Counter

s = input().strip()
freq = Counter(s)

top3 = sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:3]

for ch, count in top3:
    print(ch, count)