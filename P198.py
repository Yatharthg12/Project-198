while True:
    total = 0
    customer_name = input("Please enter your name: ")

    while True:
        Quantity = int(input("Enter the quantity of item: "))
        Items = int(input("Enter the no of items: "))
        total = Quantity*Items
        Repeat = input("Do you want to repeat this process(Y/y/N/n): ")
        if Repeat == 'y' or Repeat == 'Y':
            break
        print("_"*50)
        print("Name: ", customer_name)
        print("Total Cost: ", total)
        print()
        print("*****Thank You For Shopping With Us*****")
        print("_"*50)

        new_customer = input("Go to the next person?(Y/y/N/n): ")
        if new_customer == 'y' or new_customer == 'Y':
            break