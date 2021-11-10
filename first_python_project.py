def main():

    name = input("enter your name: ")
    print("You're name is " + name + "?")

    answer = input("yes or no? type answer here: ").lower()

    if answer == 'yes':
        print("Nice to meet you," + name )
    elif answer == 'no':
        print("THEN WHATS YOUR NAME!!!")
        main()
    else:
        print ("invalid input")

main()
