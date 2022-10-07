import random
import datetime
your_age = input("What is your ages?: ")
your_age = float(your_age)

if your_age >= 18 and your_age < 100:
    first_name = input("Enter your name: ")
    print(f"Hello {first_name.title()}, this is your number: ")
    x = datetime.datetime.now()
    print(f"Date and Time: {x}")
    print(25* "**")

    x = 1
    while x <= 5:
        print(' ' * 2, random.randint(1, 70), end=" ")
        x += 1

    print(f"\t Mega number: {random.randint(1, 25)}")
    print("\n")
    print(25 * "**")

elif your_age > 100:
    print("With your ages at present, you are belong to group of lucky people who are only 40 people of 1 million")
    print("pls, leave a lucky chance for other people!")

else:
    print("Thank you for your understanding, see you when you get older.")