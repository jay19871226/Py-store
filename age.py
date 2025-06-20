from art import tprint
import time
import sys

def loading_bar():
    print("Loading your age calculation...", end="", flush=True)
    for _ in range(10):
        time.sleep(0.3)  # Simulate some processing time
        print(".", end="", flush=True)
    print(" Done!")

def calculate_age(year_of_birth):
    current_year = 2023  # You can use datetime.datetime.now().year for dynamic current year
    return current_year - year_of_birth

def main():
    tprint("Anonymous")
    print("""
    ⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
⬛                               Anonymous                                ⬛
⬛                          Client: Public                                   ⬛
⬛                                                                         ⬛
⬛                       🎉 Welcome to Age Calculator! 🎉                  ⬛
⬛                                                                         ⬛
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
""")

    print("\n🎉 Welcome to Age Calculator! 🎉\n")
    
    # Input year of birth
    while True:
        try:
            year_of_birth = int(input("Enter the year you were born: "))
            if year_of_birth > 0:
                break
            else:
                print("Please enter a valid year!")
        except ValueError:
            print("Invalid input! Please enter a number.")
    
    # Show loading bar
    loading_bar()
    
    # Calculate age
    age = calculate_age(year_of_birth)

    # Display the result
    print(f"\n✨ You are {age} years old! 🎂\n")

if __name__ == "__main__":
    main()


