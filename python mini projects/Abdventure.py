import random
print("Welcome to this adventure")
user_name = input("Please can i have your name: ")
print(f"Hello {user_name.title()}, lets begin with the adventure")
Path = input(f"{user_name.title()} have come to an end of a dirt road there are two ways left and right what do you chose? ")
if Path == 'left':
    print("you see a taxi")
    taxi = input("Do you want to take the taxi?(Write Yes or No): ")
    if taxi == "Yes":
        print("You have got into the car.")
        print("Now the car is taking you to a farm house")
        farm_house = input("You see a old lady in the farm house.(Do you want to see her type Yes or no): ")
        if farm_house == "Yes":
            print("The old lady is telling you to visit her home")
            house = input("Do you want to go with her? ")
            if house == "Yes":
                print("Your seeing things there is no old lady there")
            if house == "No":
                print("You did the right thing there was no old lady there you were just imagining things")
                print("you keep driving down a forest")
                print("You are saw that the cars fuels about to finish. You see a patrol pump in the distance and drive to it")
                print("They are about to close but you reach it in time.")
                another_car = input("You see a person driving a is following you. do you want to stop and talk to them or keep driving(Yes or No): ")
                if another_car == "No":
                    print('Congrats that person was a kidnapper')
                    another_path = input("You have come across a another path do you want to go left or right: ")
                    if another_path == "left":
                        pass
                    if another_path == "right":
                        print("You saw a person who wants to talk to you")
                        talk = input("Do you want to talk with him (Yes or No): ")
                        if talk == "Yes":
                            print("He slowly walks towards you.")
                            print("Now he is chasing you")
                            print("Run Run RUN RUN RUNN!")
                elif another_car == "Yes":
                    print("You stop and they stop as well")
                    man = input("Hey I noticed you at the patrol pump looks like i know you from somewhere. Would you like me to take you somewhere? ")
                    if man == "No":
                        print("You did a great job, turns out that man was a kidnapper")
                    elif man == "Yes":
                        print("You notice that the mans car is full of blood in the back seat")
                        print("You realize that he is a kidnapper")
                        print("You try to run but fail")
                        print("He kidnappes and mudders you.")
                        print("You die")
    if taxi == "No".lower() or "No".title():
        print("now your walking down a road.....")
        running = input("Do you want to run to make it faster ? (say Yes or No): ")
        if running == "No":
            print("walking")
        elif running == "Yes":
            print("Running faster")
if Path == "right":
    river = input("You have come acrros a river there are two options either you swim under the river or turn right(choose right or swim)")
    if river == "swim":
        print("You have died because of the crocodiles")
    if river == "right":
        print("you have crossed the river safely")
        train = input("You have come acrros a train do you want to ride it or Walk to the left path(enter ride or left)")
        if train == "left":
            print("Sorry but you have come accros a dead-end")
        elif train == "ride":
            print("You have rided the train")
            station = input("Finally You've arrived at a station do you want to proceed to go out of the station or move to another station enter station or proceed : ")
            if station == "proceed":
                print("Now you need to go to the man who is out side the station")
                follow_man = input("Follow man say Yes")
                if follow_man == "Yes":
                    print("now following man")
                    print("you've found the man now go talk to him")
                    print("Here what to tell to the man, Hello You need to give me the key")
                    talk = input("say: ")
                    if talk == "Hello You need to give me the key":
                        print("Ahh you've come to the right place")
                        print("here is the key")
                    walk_around = input("I want you walk around the city and tell ")
                else:
                    print("Lol")
            if station == "station":
                pass
