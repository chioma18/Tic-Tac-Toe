from art import logo

print(logo)
print("Player one: X")
print("Player two: O")
b = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def board():
    design = (f"{b[0]} | {b[1]} | {b[2]}\n"
              f"---------\n"
              f"{b[3]} | {b[4]} | {b[5]}\n"
              f"---------\n"
              f"{b[6]} | {b[7]} | {b[8]}")
    print(design)

board()


def game():
    player1 = True
    n1 = n2 = []
    for i in range(9):
        try:
            if player1:
                n = int(input("Player one, select a place to play by selecting a number: ")) - 1
                if n in n2:
                    print(f"{n+1} has been taken by Player two.")
                else:
                    n1.append(n)
                    b[n] = 'X'
                    board()
                    player1 = False
            else:
                n = int(input("Player two, select a place to play by selecting a number: ")) -1
                if n in n1:
                    print(f"{n+1} has been taken by Player one.")
                else:
                    n2.append(n)
                    b[n] = 'O'
                    board()
                    player1 = True
        except IndexError:
            print("Number is out of index")

        except ValueError:
            print("You have not picked a number, please pick")

        if b[0] == b[1] == b[2] or b[3] == b[4] == b[5] or b[6] == b[7] == b[8] or \
            b[0] == b[3] == b[6] or b[1] == b[4]== b[7] or b[2] == b[5] == b[8] or \
            b[2] == b[4] == b[6] or b[0] == b[4] == b[8]:
            if player1:
                print("Oh you lost...\nPlayer two is the winner!!")
            else:
                print("Oh you lost...\nPlayer one is the winner!!")
            break
        elif i == 8:
            print("It's a draw...")
        else:
            pass

start = True
while start:
    game()

    restart = input("Type 'yes' if you want to play again or 'no' if you do not: ")
    if restart == 'no':
        start = False
        print("Goodbye! See you soon 👋")