import random

chances = 5
won = False

print("Welcome to the Guessing Game! 🎉")
print("Please choose a difficulty level:")
print("1. Easy (0-50)")
print("2. Medium (0-100)")
print("3. Hard (0-150)")

level = int(input("Enter the level (1/2/3): "))

if level == 1:
    computer_generated_number = random.randint(0, 50)
    print("You've selected Easy. Let's go!")
elif level == 2:
    computer_generated_number = random.randint(0, 100)
    print("Medium level chosen. Challenge accepted!")
elif level == 3:
    computer_generated_number = random.randint(0, 150)
    print("Brace yourself for the Hard level. Good luck!")

while chances:
    a = int(input(f"Guess the number (Chances left: {chances}): "))
    chances -= 1
    if computer_generated_number == a:
        won = True
        print(f"🎉 Congratulations! You guessed the correct number with {chances} chances left!")
        break
    elif computer_generated_number > a:
        print(f"🔼 The number is higher! Chances left: {chances}")
    else:
        print(f"🔽 The number is lower! Chances left: {chances}")

if not won:
    print(f"💔 You've used all your chances. The correct number was {computer_generated_number}. Better luck next time!")

print("Thank you for playing! 🎮")
