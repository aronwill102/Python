# The Random Quiz just demonstrates basic input and response in python

print("This is the Random Quiz that doesn't matter")

playing = input("Do you wish to play? ")

if playing != "yes":
    quit()

letsplay = input("even if it doesn't matter? ")

if letsplay != "yes":
    quit()

print("well ok...lets PLAY!!!!")

print("first question...")

answer = input("What does GPU stand for? ")
if answer == "graphics processing unit":
    print("THAT'S RIGHT")
else:
    print("WRONG!!!!")

answer = input("How much wood would a woodchuck chuck if a woodchuck could chuck wood? ")
if answer == " ":
    print("THAT'S RIGHT")
else:
    print("a woodchuck can't chuck wood")

answer = input("How many marbles are in the jar? ")
if answer == "alot":
    print("THAT'S RIGHT")
else:
    print("VERY ClOSE!!!...I think")

answer = input("If you have described something as indescribable, haven’t you already described it? ")
if answer == "you can't ":
    print("THAT'S RIGHT")
else:
    print("I'm confused...")

answer = input(" How many pennies do you think would fit into this room? ")
if answer == " alot ":
    print("THAT'S RIGHT")
else:
    print("WRONG..ish!")

answer = input("Do you think if anything is possible, it’s still possible for anything to be impossible? ")
if answer == "yes":
    print("That's deep")
else:
    print("That's impossible")

answer = input("If you punch yourself in the face and it hurts, are you weak or strong? ")
if answer == "strong":
    print("THAT'S RIGHT")
else:
    print("Why would you do that?")

answer = input("Which bear is the most condescending? ")
if answer == "A pan-duh":
    print("THAT'S RIGHT!")
else:
    print("A pan-duh!")

answer = input("What did Tennessee? ")
if answer == "The same thing as Arkansas":
    print("THAT'S RIGHT")
else:
    print("The same thing as Arkansas")

answer = input("When does a joke become a “dad joke”? ")
if answer == "When it becomes apparent":
    print("THAT'S RIGHT")
else:
    print("When it becomes apparent.")

answer = input("Why do you never see elephants hiding in trees? ")
if answer == "Because they’re so good at it":
    print("THAT'S RIGHT")
else:
    print("Because they’re so good at it.")

answer = input("What invention allows us to see through walls? ")
if answer == "Windows":
    print("THAT'S RIGHT")
else:
    print("Windows")

answer = input("What’s the least-spoken language in the world? ")
if answer == "Sign language":
    print("THAT'S RIGHT")
else:
    print("Sign language")

answer = input("What do you call a hippie’s wife? ")
if answer == "Mississippi":
    print("THAT'S RIGHT")
else:
    print("Mississippi")

answer = input("Why do cows wear bells? ")
if answer == "Because their horns don’t work":
    print("THAT'S RIGHT")
else:
    print("Because their horns don’t work")

answer = input("What do you call someone who always states the obvious? ")
if answer == "Someone who always states the obvious":
    print("THAT'S RIGHT")
else:
    print("Someone who always states the obvious")
