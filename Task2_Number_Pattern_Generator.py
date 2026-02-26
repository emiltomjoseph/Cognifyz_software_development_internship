while True:
    print("\n NUMBER PATTERN GENERATOR ")
    print("1. Increasing Triangle")
    print("2. Number Pyramid")
    print("3. Reverse Triangle")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "4":
        print("Exiting Pattern Generator. 👋")
        break

    try:
        n = int(input("Enter number of rows: "))
    except:
        print("Please enter a valid number.")
        continue

    if choice == "1":
        print("\nIncreasing Triangle:\n")
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()

    elif choice == "2":
        print("\nNumber Pyramid:\n")
        for i in range(1, n + 1):
            for space in range(n - i):
                print(" ", end="")

            for num in range(1, i + 1):
                print(num, end=" ")

            print()

    elif choice == "3":
        print("\nReverse Triangle:\n")
        for i in range(n, 0, -1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()

    else:
        print("Invalid choice. Try again.")