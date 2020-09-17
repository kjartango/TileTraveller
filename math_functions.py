option = ""
#Initial option
print("Please choose one of the options below:")
print("a. Display the sum of the first N natural numbers. ")
print("b. Display the sum of the first N Fibonacci numbers. ")
print("c. Display the approximate value of e using N terms.")
print("x. Exit from the program.\n")

while option != "x":
    option = input("Enter option: ")

    #user picks the sum of natural numbers function
    if option == "a":
        num_in = input("Enter N: ")
        if num_in.isnumeric() and int(num_in) >= 2:
            num_in_int = int(num_in)
            total = 0
            for num in range(1, num_in_int+1):
                total += num
            print("Natural number sum: ", total)
        else:
            print("Error: {} was not a valid number.".format(num_in))

    #user picks the fibonachi function
    elif option == "b":
        num_in = input("Enter N: ")
        if num_in.isnumeric() and int(num_in) >= 2:
            num_in_int = int(num_in)
            total = 1
            fib_int0 = 0
            fib_int1 = 1
            for num in range(num_in_int-2):
                fib_int1 += fib_int0
                fib_int0 = fib_int1 - fib_int0
                total += fib_int1
            print("Fibonacci sum: ", total)
        else:
            print("Error: {} was not a valid number.".format(num_in))

    #user picks the eulers number function
    elif option == "c":
        num_in = input("Enter N: ")
        if num_in.isnumeric() and int(num_in) >= 2:
            num_in_int = int(num_in)
            total = 1
            dividor = 1
            for num in range(1, num_in_int):
                dividor = dividor * num
                total += 1 / dividor
            print("Euler approximation: ", round(total, 5))
        else:
            print("Error: {} was not a valid number.".format(num_in))

    #user quits the program
    elif option == "x":
        break

    #user inputs an unrecognized option
    else:
        print("Unrecognized option " + option)
        print("Please choose one of the options below:")
        print("a. Display the sum of the first N natural numbers. ")
        print("b. Display the sum of the first N Fibonacci numbers. ")
        print("c. Display the approximate value of e using N terms.")
        print("x. Exit from the program.\n")
