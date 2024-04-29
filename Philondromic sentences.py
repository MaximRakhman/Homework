def is_palindrome(sentence):
    count = 0
    for i in range(len(sentence) // 2):
        if sentence[i] == sentence[len(sentence) - i - 1]:
            count += 1
    if count == len(sentence) // 2:
        print("The sentence is palindromic")
    else:
        print("The sentence is not palindromic")

is_palindrome("noon")
