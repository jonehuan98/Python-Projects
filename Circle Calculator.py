# function to print desired calculation results
def printResult(rad, dia, cir, are):
    print("Results:")
    print("Radius (r): {0:.2f} cm" .format(rad))
    print("Diameter (d): {0:.2f} cm" .format(dia))
    print("Circumference (C): {0:.2f} cm" .format(cir))
    print("Area (A): {0:.2f} cm" .format(are))


def getOption():
    # get input from the user for desired calculation
    optionSelect = str(input("Enter 1, to calculate diameter (d), circumference (C) and area (A), given the radius (r) of a circle" +
                    "\nEnter 2, to calculate diameter (d), area (A) and radius (r), given circumference (C) of a circle." +
                    "\nEnter 3, to calculate diameter (d), radius (r) and circumference (C), given area (A) of a circle." +
                    "\nEnter q, to exit: "))

    pi=3.14
    
    # quit if user enters q
    if (optionSelect == "q"):
        print("exit program")
        exit() 

    # calculation using given radius
    elif (optionSelect == "1"):
        # get input until it is a positive float
        while True:
            try:
                radius = float(input("Enter the value of radius (r) in centimetres: "))
                if radius > 0:
                    break
                print("Invalid value entered")
            except Exception as e:
                print(e)

        diameter = 2*radius
        circumference = 2*pi*radius
        area = pi*radius**2

    # calculation using given circumference
    elif (optionSelect == "2"):
        # get input until it is a positive float
        while True:
            try:
                circumference = float(input("Enter the value of circumference (C) in centimetres: "))
                if circumference > 0:
                    break
                print("Invalid value entered")
            except Exception as e:
                print(e)
        
        diameter = circumference/pi
        area = (circumference**2)/(4*pi)
        radius = circumference/(2*pi)

    # calculation using given area
    elif (optionSelect == "3"):
        # get input until it is a positive float
        while True:
            try:
                area = float(input("Enter the value of area (A) in centimetres: "))
                if area > 0:
                    break
                print("Invalid value entered")
            except Exception as e:
                print(e)

        import math
        radius = math.sqrt(area/pi)
        circumference = 2*pi*(math.sqrt(area/(pi)))
        diameter = 2*(math.sqrt((area/pi)))

    # prompt user to enter a valid input if input is not valid (1,2,3,q)
    else:
        print("Input error, please try again.")
        getOption()

    printResult(radius, diameter, circumference, area)
    getOption()
    # to run the calculator indefinitely for new options and values, getOption() can be added on this line.

getOption()










