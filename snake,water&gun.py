import random

def stone_snake_and_water_1():
    total_number_of_points=int(input("Total number of points(5,10,15,20) = "))
    possible_outcomes = ["Snake","Water","Gun"]

    points_of_player = 0
    points_of_computer = 0

    while points_of_computer<total_number_of_points or points_of_computer<total_number_of_points:
        player = input("Enter your object('Snake','Water','Gun') = ")
        computer = random.choice(possible_outcomes)
        print("{} x {}".format(player , computer))
        if player=="Snake" and computer=="Water":
            points_of_player+=1 
            points_of_computer+=0
        elif player=="Snake" and computer=="Gun":
            points_of_player+=0
            points_of_computer+=1
        elif player=="Snake" and computer=="Snake":
            points_of_player+=0
            points_of_computer+=0
        elif player=="Water" and computer=="Gun":
            points_of_player+=1
            points_of_computer+=0
        elif player=="Water" and computer=="Snake":
            points_of_player+=0
            points_of_computer+=1
        elif player=="Water" and computer=="Water":
            points_of_player+=0
            points_of_computer+=0
        elif player=="Gun" and computer=="Snake":
            points_of_player+=1
            points_of_computer+=0
        elif player=="Gun" and computer=="Water":
            points_of_player+=0
            points_of_computer+=1
        elif player=="Gun" and computer=="Gun":
            points_of_player+=0
            points_of_computer+=0
        print("Player : {}".format(points_of_player))
        print("Computer : {}".format(points_of_computer))    
    if points_of_player==total_number_of_points:
        print("PLAYER WINS")
    else:
        print("COMPUTER WINS")

def stone_snake_and_water_2():
    name_player1 = input("Enter player one name : ")
    name_player2 = input("Enter player two name : ")

    total_number_of_points=int(input("Total number of points(5,10,15,20) = "))
    

    points_of_player1 = 0
    points_of_player2 = 0

    for i in range(1000000):
        player1 = input("Enter your object('Snake','Water','Gun') = ")
        player2 = input("Enter your object('Snake','Water','Gun') = ")
        print("{} x {}".format(player1 , player2))
        if player1=="Snake" and player2=="Water":
            points_of_player1+=1 
            points_of_player2+=0
        elif player1=="Snake" and player2=="Gun":
            points_of_player1+=0
            points_of_player2+=1
        elif player1=="Snake" and player2=="Snake":
            points_of_player1+=0
            points_of_player2+=0
        elif player1=="Water" and player2=="Gun":
            points_of_player1+=1
            points_of_player2+=0
        elif player1=="Water" and player2=="Snake":
            points_of_player1+=0
            points_of_player2+=1
        elif player1=="Water" and player2=="Water":
            points_of_player1+=0
            points_of_player2+=0
        elif player1=="Gun" and player2=="Snake":
            points_of_player1+=1
            points_of_player2+=0
        elif player1=="Gun" and player2=="Water":
            points_of_player1+=0
            points_of_player2+=1
        elif player1=="Gun" and player2=="Gun":
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
        stone_snake_and_water_1()
    elif number_of_players == 2:
        stone_snake_and_water_2()

play_game()

play=input("Want to play again(yes/no) : ")
if play == "yes":
    play_game()
elif play == "no":
    print("Thanks for playing.")

