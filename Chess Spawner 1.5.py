import random

def chess_game():

    x = "y"

    while (x == "y"):

        letters = ['A','B','C','D','E','F','G','H']
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8']
        numbers1 = ['2', '3', '4', '5', '6', '7']
        pieces1 = ['Rook1', 'Bishop2', 'Knight2', 'Queen']
        pieces2 = ['Rook1', 'Bishop2', 'Knight2', 'Queen']
        pawn1 = ['Pawn1', 'Pawn2', 'Pawn3', 'Pawn4', 'Pawn5', 'Pawn6', 'Pawn7', 'Pawn8', 'Rook2', 'Bishop1', 'Knight1']
        pawn2 = ['Pawn1', 'Pawn2', 'Pawn3', 'Pawn4', 'Pawn5', 'Pawn6', 'Pawn7', 'Pawn8', 'Rook2', 'Bishop1', 'Knight1']
        colour = ['Black', 'White']
        positions = []
        positions2 = []
        inc = 0

        for i in range(len(letters)):
            for j in range(len(numbers)):
                newPos = letters[i] + numbers[j]
                positions.insert(inc, newPos)
                inc += 1

        for q in range(len(letters)):
            for s in range(len(numbers1)):
                newPos2 = letters[q] + numbers1[s]
                positions2.insert(inc, newPos2)
                inc += 1

        print('White:')
        print()

        for k in range(2):
            elem = random.choice(pieces1)
            elem1 = random.choice(pawn1)
            pieces1.remove(elem)
            pawn1.remove(elem1)
            pos = random.choice(positions)
            pos1 = random.choice(positions2)
            positions.remove(pos)
            positions2.remove(pos1)
            print(elem, 'at', pos)
            print(elem1, 'at', pos1)

        for m in range(1):
            pos = random.choice(positions)
            pos1 = random.choice(positions2)
            positions.remove(pos)
            positions2.remove(pos1)
            print('King at', pos, 'or', pos1)

        print()
        print('Black:')
        print()

        for k in range(2):
            elem = random.choice(pieces2)
            elem1 = random.choice(pawn2)
            pieces2.remove(elem)
            pawn2.remove(elem1)
            pos = random.choice(positions)
            pos1 = random.choice(positions2)
            positions.remove(pos)
            positions2.remove(pos1)
            print(elem, 'at', pos)
            print(elem1, 'at', pos1)

        for t in range(1):
            pos = random.choice(positions)
            pos1 = random.choice(positions2)
            positions.remove(pos)
            positions2.remove(pos1)
            print('King at', pos, 'or', pos1)
            

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
