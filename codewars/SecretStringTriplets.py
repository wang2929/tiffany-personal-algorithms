def recover_secret(triplets):
    letters = list(set([l for t in triplets for l in t]))
    change = True
    while change:
        change = False
        for t in triplets:
            for i in range(0, 2):
                a, b = letters.index(t[i]), letters.index(t[i+1])
                if a > b:
                    letters[a], letters[b] = letters[b], letters[a]
                    change = True
    return ''.join(letters)

if __name__ == '__main__':
    triplets = [
          ['t','u','p'],
          ['w','h','i'],
          ['t','s','u'],
          ['a','t','s'],
          ['h','a','p'],
          ['t','i','s'],
          ['w','h','s']
        ]
    print(recover_secret(triplets)) # whatisup
    triplets = [
            ['t', 'u', 'p'], 
            ['w', 'h', 'i'], 
            ['t', 's', 'u'], 
            ['a', 't', 's'], 
            ['h', 'a', 'p'], 
            ['t', 'i', 's']
        ]
    print(recover_secret(triplets)) # whatisup
    
    triplets = [
            ['t', 's', 'f'], 
            ['a', 's', 'u'], 
            ['m', 'a', 'f'], 
            ['a', 'i', 'n'], 
            ['s', 'u', 'n'], 
            ['m', 'f', 'u'], 
            ['a', 't', 'h'], 
            ['t', 'h', 'i'], 
            ['h', 'i', 'f'], 
            ['m', 'h', 'f'], 
            ['a', 'u', 'n'], 
            ['m', 'a', 't'], 
            ['f', 'u', 'n'], 
            ['h', 's', 'n'], 
            ['a', 'i', 's'], 
            ['m', 's', 'n'], 
            ['m', 's', 'u']
        ]
    print(recover_secret(triplets)) # mathisfun
    