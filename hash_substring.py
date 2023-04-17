def read_input():
    source = input().strip()
    if source == 'F':
        with open('test.txt', 'r') as f:
            pattern = f.readline().strip()
            text = f.readline().strip()
    elif source == 'I':
        pattern = input().strip()
        text = input().strip()
    else:
        print("Invalid input source")
        exit()
    return pattern, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    occurrences = []
    p_len = len(pattern)
    t_len = len(text)

    
    p_hash = sum([ord(pattern[i]) * (101 ** i) for i in range(p_len)]) % 10**9 + 7
    t_hash = sum([ord(text[i]) * (101 ** i) for i in range(p_len)]) % 10**9
    
    for i in range(t_len - p_len + 1):
        if p_hash == t_hash:
            if text[i:i+p_len] == pattern:
                occurrences.append(i)
        if i < t_len - p_len:
            
            t_hash = (t_hash - ord(text[i]) * (101 ** (p_len - 1))) % 10**9
            t_hash = (t_hash * 101 + ord(text[i+p_len])) % 10**9

    return sorted(occurrences)

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
