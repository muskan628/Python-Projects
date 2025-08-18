import random
print("Number Guessing Game...")

#Taking the start and end range from the user
start_range=int(input("Enter the Start range: "))
end=int(input("Enter the End range: "))

print(f"Think of a number between {start_range} and {end}. I will try to guess it!")
print()

def guess_no(start_range,end):

    mid=(start_range+end)//2
    print(f"Is the Number: {mid}")
    user_input=input("Enter Yes or No: ").lower()
    if user_input=="yes":
        print("Congratulations....")
        exit()
    
    elif user_input=="no":
        print(f"Is the no greater than {mid}")
        user_input=input("Enter Yes or No: ").lower()
        print()
        if user_input=="yes":
            guess_no(mid+1,end)

        elif user_input=="no":
            guess_no(start_range,mid-1)

        else:
            print("Invalid input. Please enter yes or no...")

    else:
            print("Invalid input. Please enter yes or no...")

guess_no(start_range,end)

