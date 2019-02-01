fname = input("Enter file name: ")
i=1
with open(fname, 'r') as f:
    for line in f:
        num_words=0
        letters=0
        words = line.split()
        num_words += len(words)
        for c in line:
            if c.isalpha():
                letters=letters+1
            else:
                pass
        print('Number of words in line' ,i )
        print(num_words)
        print('Number of letters in line', i)
        print(letters)
        i=i+1
