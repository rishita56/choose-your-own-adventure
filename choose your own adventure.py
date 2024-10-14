name=input("Type Your Name: ")
print("Welcome!",name,"to this exciting game!")
print("Let's start")
answer=input("Do you wanna go left or right? type left or right ").lower()

if answer== "left":
    answer=input("You reached the river. You can walk arounf it or swim across it.Type walk or swim ").lower()

    if answer=="walk":
        print("You walked for many miles, ran out of water and lost!")
    elif answer=="swim":
        print("You swam across and got eaten by alligator")
    else:
         print("Not a valid option.You Loose!!")  

elif answer=="right":
    answer=input("You come to a bridge, looks wobbly, wanna cross or walk by?type cross or walk ").lower()

    if answer=="back":
        print("You lost!")
    elif answer=="walk":
        answer=input("You crossed the bridge and met a stranger.Wanna talk(yes/no)? ")

        if answer== "yes":
            print("You talk to stranger and they give you gold.YOU WIN!")
        elif answer=="no":
            print("You ignored the stranger and they get offended and YOU LOOSE!")
        else:
            print("Not a valid option.You Loose!!")  

else:
    print("Not a valid option.You Loose!!") 

print("Thank you!")       