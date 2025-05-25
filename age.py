try:
    age = int(input("Enter your age: "))

    if age%2 == 0:
        print("Your age is even")
    else:
        print("Your age is odd")

except ValueError:
    print("Invalid input")

else:
    print("No errors")

finally:
    print("This code will execute no matter what")