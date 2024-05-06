import sys

def count_words(filePath):
    wordCount = {}
    with open(filePath, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                word = word.lower()
                if word in wordCount:
                    wordCount[word] += 1
                else:
                    wordCount[word] = 1
    return wordCount

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py <filePath>")
        sys.exit(1)
    
    filePath = sys.argv[1]
    wordCount = count_words(filePath)
    
    sortedWordCount = sorted(wordCount.items(), key=lambda x: x[1])
    
    if len(sortedWordCount) < 10:
        n = len(sortedWordCount)
    else:
        n = 10
    
    print(f"Top {n} most common words:")
    for word, count in sortedWordCount[-n:]:
        print(f"{word}: {count}")
