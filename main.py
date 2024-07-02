MAX_LINES= 3;


def deposit():
    while True:
        amount = input("Enter the amount you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero")
        else:
            print("Please enter a number")

    return amount

def main():
  balance= deposit()


main()