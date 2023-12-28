import random

def rock_paper_and_scissors_1():
    total_number_of_points=int(input("Total number of points(5,10,15,20) = "))
    possible_outcomes = ["Rock","Paper","Scissor"]

    points_of_player = 0
    points_of_computer = 0

    while points_of_computer<total_number_of_points or points_of_computer<total_number_of_points:
        player = input("Enter your object('Rock','Paper','Scissor') = ")
        computer = random.choice(possible_outcomes)
        print("{} x {}".format(player , computer))
        if player=="Rock" and computer=="Scissor":
            points_of_player+=1 
            points_of_computer+=0
        elif player=="Rock" and computer=="Paper":
            points_of_player+=0
            points_of_computer+=1
        elif player=="Rock" and computer=="Rock":
            points_of_player+=0
            points_of_computer+=0
        elif player=="Scissor" and computer=="Paper":
            points_of_player+=1
            points_of_computer+=0
        elif player=="Scissor" and computer=="Rock":
            points_of_player+=0
            points_of_computer+=1
        elif player=="Scissor" and computer=="Scissor":
            points_of_player+=0
            points_of_computer+=0
        elif player=="Paper" and computer=="Rock":
            points_of_player+=1
            points_of_computer+=0
        elif player=="Paper" and computer=="Scissor":
            points_of_player+=0
            points_of_computer+=1
        elif player=="Paper" and computer=="Paper":
            points_of_player+=0
            points_of_computer+=0
        print("Player : {}".format(points_of_player))
        print("Computer : {}".format(points_of_computer))    
    if points_of_player==total_number_of_points:
        print("PLAYER WINS")
    else:
        print("COMPUTER WINS")

def rock_paper_and_scissors_2():
    name_player1 = input("Enter player one name : ")
    name_player2 = input("Enter player two name : ")

    total_number_of_points=int(input("Total number of points(5,10,15,20) = "))
    

    points_of_player1 = 0
    points_of_player2 = 0

    for i in range(1000000):
        player1 = input("Enter your object('Rock','Paper','Scissor') = ")
        player2 = input("Enter your object('Rock','Paper','Scissor') = ")
        print("{} x {}".format(player1 , player2))
        if player1=="Rock" and player2=="Scissor":
            points_of_player1+=1 
            points_of_player2+=0
        elif player1=="Rock" and player2=="Paper":
            points_of_player1+=0
            points_of_player2+=1
        elif player1=="Rock" and player2=="Rock":
            points_of_player1+=0
            points_of_player2+=0
        elif player1=="Scissor" and player2=="Paper":
            points_of_player1+=1
            points_of_player2+=0
        elif player1=="Scissor" and player2=="Rock":
            points_of_player1+=0
            points_of_player2+=1
        elif player1=="Scissor" and player2=="Scissor":
            points_of_player1+=0
            points_of_player2+=0
        elif player1=="Paper" and player2=="Rock":
            points_of_player1+=1
            points_of_player2+=0
        elif player1=="Paper" and player2=="Scissor":
            points_of_player1+=0
            points_of_player2+=1
        elif player1=="Paper" and player2=="Paper":
            points_of_player1+=0
            points_of_player2+=0


        print("{} : {}".format(name_player1 , points_of_player1))
        print("{} : {}".format(name_player2 , points_of_player2))

        if points_of_player1==total_number_of_points or points_of_player2==total_number_of_points:
            break

    if points_of_player1==total_number_of_points:
        print("{} WINS".format(name_player1))
    else:
        print("{} WINS".format(name_player2))

def play_game():
    number_of_players = int(input("Single player(1) or Double player(2) : "))
    if number_of_players == 1:
        rock_paper_and_scissors_1()
    elif number_of_players == 2:
        rock_paper_and_scissors_2()

play_game()

play=input("Want to play again(yes/no) : ")
if play == "y":
    play_game()
elif play == "n":
    print("Thanks for playing.")

