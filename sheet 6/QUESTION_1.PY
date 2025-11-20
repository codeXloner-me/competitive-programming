VOWELS = "aeiouAEIOU"
input_strings = ["List", "Apple"]
for S in input_strings:
    vowel_count = 0
    consonant_count = 0
    for char in S:
        if char.isalpha(): 
            if char in VOWELS:
                vowel_count += 1
            else:
                consonant_count += 1
    print(f"{vowel_count}{consonant_count}")