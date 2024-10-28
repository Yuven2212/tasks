def find_pattern_occurrences(text, pattern):
    text_len = len(text)
    pattern_len = len(pattern)
    indices = []

    
    for i in range(text_len - pattern_len + 1):
        match = True
       
        for j in range(pattern_len):
            if text[i + j] != pattern[j]:
                match = False
                break
        
        if match:
            indices.append(i)

    return indices

text = "abababab"
pattern = "aba"
print(find_pattern_occurrences(text, pattern))
