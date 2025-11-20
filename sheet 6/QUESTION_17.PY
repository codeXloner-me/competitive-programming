A = "aeiOUz"
vowels = "aeiou"
S = A + A 
temp_S = ""
for char in S:
    if 'a' <= char <= 'z': 
        temp_S += char
S = temp_S 
result = ""
for char in S:
    if char in vowels:
        result += '#'
    else:
        result += char
        
print(result) 