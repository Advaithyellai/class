a = input("Type a sentence(space before punchuation)  ")
a = a.lower()
e = 0
b = a.split()
c = len(b)
for x in range(0, c):
    f = list(a)
    if f[-1] == '.':
        e = 1
    elif f[-1] == '!':
        e = 2
    elif f[-1] == '?':
        e = 3
    if b[x] == 'this':
        if b[x-1] == 'is':
            print(b[x], "is a demonstrative pronoun")
        elif b[x-1] == 'has':
            print(b[x], "is a demonstrative pronoun")
        elif b[x-1] == 'had':
            print(b[x], "is a demonstrative pronoun")
        elif b[x-1] == 'have':
            print(b[x], "is a demonstrative pronoun")
        else:
            print(b[x], "is a demonstrative adjective")
    elif b[x] == 'that':
        if b[x-1] == 'is':
            print(b[x], "is a demonstrative pronoun")
        elif b[x-1] == 'has':
            print(b[x], "is a demonstrative pronoun")
        elif b[x-1] == 'had':
            print(b[x], "is a demonstrative pronoun")
        elif b[x-1] == 'have':
            print(b[x], "is a demonstrative pronoun")
        else:
            print(b[x], "is a demonstrative adjective")
    elif b[x] == 'these':
        if b[x-1] == 'is':
            print(b[x], "is a demonstrative pronoun")
        elif b[x-1] == 'has':
            print(b[x], "is a demonstrative pronoun")
        elif b[x-1] == 'had':
            print(b[x], "is a demonstrative pronoun")
        elif b[x-1] == 'have':
            print(b[x], "is a demonstrative pronoun")
        else:
            print(b[x], "is a demonstrative adjective")
    elif b[x] == 'those':
        if b[x-1] == 'is':
            print(b[x], "is a demonstrative pronoun")
        elif b[x-1] == 'has':
            print(b[x], "is a demonstrative pronoun")
        elif b[x-1] == 'had':
            print(b[x], "is a demonstrative pronoun")
        elif b[x-1] == 'have':
            print(b[x], "is a demonstrative pronoun")
        else:
            print(b[x], "is a demonstrative adjective")
    else:
        if b[x-1] == 'the':
            print(b[x], "is the noun")
        elif b[x-1] == 'a':
            print(b[x], "is the noun")
        elif b[x-1] == 'an':
            print(b[x], "is the noun")
        else:
            d = list(b[x])
            if d[-2:-1] == 'er':
                print(b[x], "is a noun")
            else:
                if d[-3:-1] == 'ing':
                    if b[x-1] == 'will':
                        print(b[x], "is a verb at future tense")
                    elif b[x-1] == 'shall':
                        print(b[x], "is a verb at future tense")
                    else:
                        print(b[x], "is a verb at present tense")
                elif d[-2: -1] == 'ed':
                    print(b[x], "is a verb at past tense")
                elif b[x-1] == 'will':
                    print(b[x], "is a verb at future tense")
                elif b[x-1] == 'shall':
                    print(b[x], "is a verb at future tense")
                else:
                    if b[x] == 'the':
                        print("'The' is an article")
                    elif b[x] == 'a':
                        print("'A' is an article")
                    elif b[x] == 'an':
                        print("'An' is an article")
                    else:
                        pass