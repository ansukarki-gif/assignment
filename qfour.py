sentence = (input ("Enter a Sentence:"))

sentence = " ".join(sentence.split()).lower()

words = sentence.split()

word_count = len(words)

python_count = words.count("python")

longest_word = max(words, key=len)

print("Sentence:", sentence)
print("Total Words:", word_count)
print("python Appears:", python_count, "times")
print("Longest Word:", longest_word)
