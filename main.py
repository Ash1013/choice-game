# Hi, this is a multiple choice game wich moves based on your choice
print("Welcome to my first game")
name = input("Enter your name : ")
age = int(input("Enter your age : "))
health = 10
print("Ok", name, "you are", age, "years old")
if age >= "10" and age <= "100":
    print("You are old enough to play")
    want_to_play = input("Do you want to play? [yes/no] : ")
    if want_to_play.lower() == "yes":
        print("Ok", name, "you are starting with", health, "health")
        print("Let's start")
        dir1 = input(
            name + " you are standing on a junction, lost. You see two ways what will you choose? Left or right : ")
        if dir1.lower() == "right":
            dir2 = input("Ok. Now you see a river. Do you want to go around or across it ? : ")
            if dir2.lower() == "across":
                print("You have been bit by a fish so your health is", health - 2)
                dir3 = input("Now you see a house from which a girl is crying. Would you save her or not? : ")
                if dir3.lower() == "yes":
                    print("You have been hit by a psycho killer. So your heath is", health - 2)
                    print("Wow, you've reached your destination")
            if dir2.lower() == "around":
                dir4 = input("Now you see a house from which a girl is crying. Would you save her or not? : ")
                if dir4.lower() == "no":
                    print("That's cruel, but ok")
                    print("Wow, you've reached your destination")

        if dir1.lower() == "left":
            print("Oops! You fell down the cliff and died")
    if health == 0:
        print("Game over")
    if want_to_play.lower() == "no":
        print("Ok,as you wish. Bye...")

if age > "100":
    print("This is not a valid age " + name)
if age < "10":
    print("You are not eligible to play this game " + name)
