sentence = input("Enter a sentence: ")
words = sentence.split()
LWord = ''
MLen = 0

for word in words:
    if len(word) > MLen:
        LWord = word
        MLen = len(word)

print("The longest word in the sentence is:", LWord)
