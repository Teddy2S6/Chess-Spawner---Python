import random

def chess_game():

    x = "y"

    while (x == "y"):

        letters = ['A','B','C','D','E','F','G','H']
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8']
        pieces1 = ['Pawn1', 'Pawn2', 'Pawn3', 'Pawn4', 'Pawn5', 'Pawn6', 'Pawn7', 'Pawn8', 'Rook1', 'Rook2', 'Bishop1', 'Bishop2', 'Knight1', 'Knight2', 'Queen']
        pieces2 = ['Pawn1', 'Pawn2', 'Pawn3', 'Pawn4', 'Pawn5', 'Pawn6', 'Pawn7', 'Pawn8', 'Rook1', 'Rook2', 'Bishop1', 'Bishop2', 'Knight1', 'Knight2', 'Queen']
        colour = ['Black', 'White']
        positions = []
        inc = 0

        for i in range(len(letters)):
            for j in range(len(numbers)):
                newPos = letters[i] + numbers[j]
                positions.insert(inc, newPos)
                inc += 1

        print('White')
        print()

        for k in range(4):
            elem = random.choice(pieces1)
            pieces1.remove(elem)
            pos = random.choice(positions)
            positions.remove(pos)
            print(elem, 'at', pos)

        for m in range(1):
            pos = random.choice(positions)
            positions.remove(pos)
            print('King at', pos)

        print()
        print('Black')
        print()

        for c in range(4):
            elem = random.choice(pieces2)
            pieces2.remove(elem)
            pos = random.choice(positions)
            positions.remove(pos)
            print(elem, 'at', pos)

        for t in range(1):
            pos = random.choice(positions)
            positions.remove(pos)
            print('King at', pos)

        print()

        for p in range(1):
            start = random.choice(colour)
            print(start, 'starts')

        
        print()
        x = str(input("Would you like a diffrent set up [y/n]: "))
        x.lower().strip()
        print()

        if (x == "n"):
            print("Okay. Have fun!")
            break

        else:
            while (x != "y" or x != "n"):
                if (x == "y"):
                    print("Let the fun continue!")
                    break
                print()
                print("Enter yes or no")
                x = str(input("Would you like a diffrent set up [y/n]: "))
                x.lower().strip()
                print()

                if (x == "n"):
                    print("Okay. Have fun!")
                    break

chess_game()
