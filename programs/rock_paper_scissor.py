def check_turn(player1_choice, player2_choice):
    global score1
    global score2
    if player1_choice == player2_choice:
        print("choice should not be same ")
        score1 += 0
        score2 += 0
    elif (player1_choice.lower() == "rock" and player2_choice.lower() == "scissor") or \
         (player1_choice.lower() == "paper" and player2_choice.lower() == "rock") or \
         (player1_choice.lower() == "scissor" and player2_choice.lower() == "paper"):
        score1 = score1+1
        
    else:
        score2 = score2+1

score1=0
score2=0
for i in range(1,4):
    print("1->Rock, 2->Paper, 3->Scissor")
    turn1 = input("Player 1, enter input as mentioned ")
    turn2 = input("Player 2, enter input as mentioned ")

    check_turn(turn1, turn2)

if score1 > score2:
    print("Player1 won with score: ",score1)
else:
    print("player2 won with score: ",score2)


