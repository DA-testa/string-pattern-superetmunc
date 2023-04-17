# python3

def read_input():
    source = input().strip()
    if source == 'F':
        with open('test.txt', 'r') as f:
            pattern = f.readline().strip()
            text = f.readline().strip()
    elif source == 'I':
        pattern = input().strip()
        text = input().strip()
    return pattern, text
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    occurrences = []
    p_len = len(pattern)
    t_len = len(text)

    # Calculate the hash value of the pattern and the first window of the text.
    p_hash = sum([ord(pattern[i]) * (101 ** i) for i in range(p_len)]) % 10**9 + 7
    t_hash = sum([ord(text[i]) * (101 ** i) for i in range(p_len)]) % 10**9
    
    for i in range(t_len - p_len + 1):
        if p_hash == t_hash:
            if text[i:i+p_len] == pattern:
                occurrences.append(i)
        if i < t_len - p_len:
            # Update the hash value of the next window.
            t_hash = (t_hash - ord(text[i]) * (101 ** (p_len - 1))) % 10**9
            t_hash = (t_hash * 101 + ord(text[i+p_len])) % 10**9

    # and return an iterable variable
    return occurrences


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

