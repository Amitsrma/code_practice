def minion_game(string):
    # your code goes here
    n = len(string)
    vowels = ['A','E','I','O','U']#{'A':1,'E':1,'I':1,'O':1,'U':1}
    stuart = 0 #consonants
    kevin = 0 #Vowels
    for index, character in enumerate(string):
        if character in vowels:
            kevin += n-index
        else:
            stuart += n-index
    if kevin > stuart:
        print(f"Kevin {kevin}")
    elif kevin < stuart:
        print(f'Stuart {stuart}')
    else:
        print("Draw")