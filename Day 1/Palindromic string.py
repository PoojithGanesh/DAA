def first_palindromic_string(words):
    for word in words:
        if word == word[::-1]:
            return word
    return ""
words = ["abc", "car", "ada", "racecar", "cool"]
result = first_palindromic_string(words)
print(result)  
