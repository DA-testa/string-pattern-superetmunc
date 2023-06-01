def read_input():
    input_type = input().rstrip()

    if input_type == "I":
        pattern = input().rstrip()
        text = input().rstrip()
    elif input_type == "F":
        file_path = "06"
        with open(f"tests/{file_path}", "r") as file:
            pattern = file.readline().rstrip()
            text = file.readline().rstrip()
    
    return pattern, text

def print_occurrences(occurrences):
    print(' '.join(map(str, occurrences)))

def get_hash(string):
    Q, B = 256, 13
    length = len(string)
    string_hash = 0
    for i in range(length):
        unicode_value = ord(string[i])
        string_hash = (B * string_hash + unicode_value) % Q
    return string_hash

def get_occurrences(pattern, text): 
    Q, B = 256, 13
    pattern_length, text_length = len(pattern), len(text)
    multiplier = 1
    for i in range(1, pattern_length):
        multiplier = (multiplier * B) % Q
    pattern_hash = get_hash(pattern)
    text_hash = get_hash(text[:pattern_length])
    positions = []
    for i in range(text_length - pattern_length + 1):
        if pattern_hash == text_hash and pattern == text[i:i+pattern_length]:
            positions.append(str(i))
        if i < text_length - pattern_length:
            first_char_unicode = ord(text[i])
            last_char_unicode = ord(text[i+pattern_length])
            text_hash = ((text_hash - first_char_unicode * multiplier) * B + last_char_unicode) % Q
    return positions

if __name__ == '__main__':
    occurrences = get_occurrences(*read_input())
    print_occurrences(occurrences)
