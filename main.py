# Choose Your Own Adventure Game

name = input("Enter your name: ").strip().upper()
print(f"\nWELCOME {name}!")

print("\nYou are on a dirt road. It has come to an end.")
answer = input("Do you want to go LEFT or RIGHT? \n").strip().lower()

if answer == "left":

    print("\nYou entered an amusement park!")
    choice = input("Do you want to ride the FERRIS WHEEL or ROLLER COASTER? \n").strip().lower()

    if choice == "roller coaster":

        again = input("You rode the roller coaster! 🎢\nType 'ride' to ride again or 'go back': \n").strip().lower()

        if again == "ride":
            print("\nYou ride again and have lots of fun! 🎉 YOU WIN!")
        elif again == "go back":
            print("\nYou left the park. YOU LOSE!")
        else:
            print("\nInvalid choice. YOU LOSE!")

    elif choice == "ferris wheel":
        print("\nYou enjoyed the beautiful view from the ferris wheel! 🎡 YOU WIN!")

    else:
        print("\nInvalid choice. YOU LOSE!")

elif answer == "right":

    print("\nYou see a small scary hut.")
    hut = input("Do you want to ENTER or NOT? \n").strip().lower()

    if hut == "enter":
        print("\nYou entered and found treasure! 🏆 YOU WIN!")
    elif hut == "not":
        print("\nYou ran away. YOU LOSE!")
    else:
        print("\nInvalid choice. YOU LOSE!")

else:
    print("\nInvalid path. YOU LOSE!")