word = input("Type a word  ")
word = word.lower()
characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for char in word:
  for i in range(0, 27):
    if char == characters[i]:
      counts[i] = counts[i] + 1
for a in range(0, 27):
  if characters[a] == " ":
    characters[a] = "space"
  print("There are %d %s's in the word" % (counts[a], characters[a]))