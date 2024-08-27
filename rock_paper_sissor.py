import random 

def play():
    print("Let's play the game Rock-Paper-Sissor !!!")
    print("'r' for Rock, 'p' for Paper, 's' for Sissor")
    
    player = input("Enter your choice: ")
    computer = random.choice(['r','p','s'])

    print("Player v/s Opponent")
    print("Player: ",player)
    print("Opponent: ",computer)


    if player == computer:
        print("It's a Tie !") 
    elif is_win(player, computer):
        print("You Won :)") 
    else:
        print("You Lost :(") 

def is_win(p,c):
    # r>s s>p p>r
    # return True if the player wins
    if (p=='r' and c=='s') or (p=='s' and c=='p') or (p=='p' and c=='r') :
        return True

play()