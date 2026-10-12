day = int(input("Enter day of week (1-4): "))

match day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case _:
        print("Invalid")
