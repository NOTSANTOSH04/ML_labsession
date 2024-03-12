word = input("Enter the word: ")
# Function to count occurrences of each character in a word
def Word_OCC(word):
    dict = {}
    for i in word:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict
# Function to find the character with the maximum count
def MaxWord(dict):
    maxVal = 0
    maxKey = None
    for key, value in dict.items():
        if value > maxVal:
            maxVal = value
            maxKey = key
    return maxVal, maxKey

max_count, max_char = MaxWord(Word_OCC(word))
print(f"The maximum occurring character is '{max_char}' with a count of {max_count}")