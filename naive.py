# text="ABABDABACDABABCABAB"
# pat="ABABC"

# n=len(text)
# m=len(pat)

# for i in range(n-m+1):
#     j=0
#     while j<m and text[i+j]==pat[j]:
#         j+=1
#     if j==m:
#         print("Pattern found at index",i) 

def naive(s, pat):
    n = len(s)
    m = len(pat)
    if n < m:
        return -1
    for i in range(n - m + 1):  # iterate over all possible starting positions
        match = True
        for j in range(m):  # check each character of pattern
            if s[i + j] != pat[j]:
                match = False
                break
        if match:
            return i  # return starting index of match
    return -1

# Example usage
s = "hello world"
pat = "world"
print(naive(s, pat))  # True

