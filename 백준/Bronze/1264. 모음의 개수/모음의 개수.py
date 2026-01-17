while True:
  vowel = 0
  sentence = input() 
  if sentence == "#": 
    break 
  sentence = sentence.lower()
  for letter in sentence:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
      vowel = vowel + 1
  print(vowel)