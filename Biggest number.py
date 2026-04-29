def biggestNumber():
    first_number = int(input("Въведи първото число: "))
    second_number = int(input("Въведи второ число: "))

    if first_number >= second_number:
        print(first_number)
    else:
        print(second_number)

biggestNumber()