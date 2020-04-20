def hangman(word):
    wrong = 0
    stages = ["",
             "______      ",
             "|           ",
             "|     |     ",
             "|     O     ",
             "|    /|\    ",
             "|    / \    ",
             "|           "
             ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ")
    while wrong < len(stages) -1:
        print("\n")
        msg = "1文字を予想してください"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You Win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("you lose. 正解は {}.".format(word))

# hangman("puma")

import random
rdi = random.randint(0,2)
word_list = ["hell", "dead or alive","heaven"]

hangman(word_list[rdi])
