def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

def c_to_k(c):
    return c + 273.15

def k_to_c(k):
    return k - 273.15

def f_to_k(f):
    return c_to_k(f_to_c(f))

def k_to_f(k):
    return c_to_f(k_to_c(k))


while True:
    print("\n Complete Temperature Converter ")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

    choice = input("Choose an option (1-7): ")

    if choice == "7":
        print("Exiting program. Goodbye! 👋")
        break

    if choice in ["1", "2", "3", "4", "5", "6"]:
        try:
            temp = float(input("Enter temperature value: "))

            if choice == "1":
                result = c_to_f(temp)
                print(f"{temp}°C = {result:.2f}°F")

            elif choice == "2":
                result = f_to_c(temp)
                print(f"{temp}°F = {result:.2f}°C")

            elif choice == "3":
                result = c_to_k(temp)
                print(f"{temp}°C = {result:.2f}K")

            elif choice == "4":
                result = k_to_c(temp)
                print(f"{temp}K = {result:.2f}°C")

            elif choice == "5":
                result = f_to_k(temp)
                print(f"{temp}°F = {result:.2f}K")

            elif choice == "6":
                result = k_to_f(temp)
                print(f"{temp}K = {result:.2f}°F")

        except ValueError:
            print("Invalid input! Please enter a numeric value.")

    else:
        print("Invalid choice! Please select between 1 and 7.")