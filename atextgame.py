print("Welcome to play a game: ")
name = input("What is your name? ")
age = int(input("What is your age? "))
print("Hello ", name, " you are ", age, " years old. ")

def letsPlay():
    health = 10
    print("You are starting with ", health, " health")
    leftOrRight = input("Choose your path, left or right ").lower()
    if(leftOrRight == "left"):
        ans = input("How you are going to cross the lake (across/around): ").lower();
        if ans == "around":
            print("You successfully reached the other side of the lake. ")
            print("You Win ")
        elif ans == "across":
            print("You managed to swim acros to the other side of the lake. But, you lost 5 health in the process.")
            health -= 5
            print("You are having now ", health, " health")
            if(health == 0):
                print("You don't have enough health to play, you lost")
            else: print("You survived, you win!")
    
    else:
        print("You chose a wrong path. You lost. ")

if age >= 18:
    print("You are old enough!")
    doYouWantToPlay = input("Do you want to play?").lower()
    if(doYouWantToPlay == "yes"):
        print("Let's Play")
        letsPlay()
    elif (doYouWantToPlay == "no"):
        print("bye....")

elif age >= 14:
    print("You can play with proper supervision")
    doYouWantToPlay = input("Do you want to play?").lower()
    if(doYouWantToPlay == "yes"):
        print("Let's Play")
        letsPlay()
    elif (doYouWantToPlay == "no"):
        print("bye....")
else:
    print("You are not allowed to play")



