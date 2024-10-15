def findSubstrings(words):
    result = set() 
    for i in range(len(words)):
        for j in range(len(words)):
            if i != j and words[i] in words[j]:
                result.add(words[i])
    return list(result)
# Test cases
print(findSubstrings(["mass", "as", "hero", "superhero"]))  # Output: ["as", "hero"]
print(findSubstrings(["leetcode", "et", "code"]))          # Output: ["et", "code"]
print(findSubstrings(["blue", "green", "bu"]))             # Output: []
