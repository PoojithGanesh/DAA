def strStr(haystack, needle):
    if not needle:
        return 0
    haystack_len = len(haystack)
    needle_len = len(needle)
    for i in range(haystack_len - needle_len + 1):
        # Check if the substring matches
        if haystack[i:i + needle_len] == needle:
            return i   
    return -1  
# Test cases
print(strStr("sadbutsad", "sad"))   # Output: 0
print(strStr("leetcode", "leeto"))   # Output: -1
