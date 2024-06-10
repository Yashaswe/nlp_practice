import re

regexp = re.compile(r"ab[^\s]*cd")

phrases = ["abcd", "xabcdxx", "aaa abxxxcd ccc" ,"ab cd"]
matches = []

for phrase in phrases:
  if re.search(regexp, phrase):
    matches.append(phrase)

print(matches)

regexp2 = re.compile(r"\bstory\b|\bbooks\b|\bbread\b")

phrases2 = ["I like history", "I like story books", "I like to eat bread" ,"eat"]
matches2 = []

for phrase in phrases2:
  if re.search(regexp2, phrase):
    matches2.append(phrase)

print(matches2)