
def num_check(question):

    valid = False
    while not valid:

        error = "Please enter a number that is more than zero"

        try:

            response = float(input(question))

            if response > 0:
                return response


            else:
                print("Please enter a number that is more than zero")
                print()


        except ValueError:
            print(error)

keep_going = ""
while keep_going == "":

    width = num_check("Width: ")
    height = num_check("Height: ")

    area = width * height
    perimeter = 2 * (width + height)

    print("Perimeter: {} units".format(perimeter))
    print("Area: {} square units".format(area))

    keep_going = input("Press <enter> to keep going or any to quit")

print()
print("Thanks for using the area / perimeter calculator")

