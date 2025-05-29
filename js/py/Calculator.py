def add(first_number, second_number):
    return first_number + second_number

def subtract(first_number, second_number):
    return first_number - second_number

def multiply(first_number, second_number):
    return first_number * second_number

def divide(first_number, second_number):
    if second_number == 0:
        return "Syntax-Error: Zero Division"
    return first_number / second_number

def calculator():
    while True: 
        try:
            first_number = float(input("Enter the first number: "))
            second_number = float(input("Enter the second number: "))
            return first_number, second_number
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

def main():
    while True:
        first_number, second_number = calculator()
        while True:
            print("\nSelect an operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")

            operation = input("Enter operation (1/2/3/4): ")

            if operation == '1':
                print(f"{first_number} + {second_number} = {add(first_number, second_number)}")
            elif operation == '2':
                print(f"{first_number} - {second_number} = {subtract(first_number, second_number)}")
            elif operation == '3':
                print(f"{first_number} * {second_number} = {multiply(first_number, second_number)}")
            elif operation == '4':
                result = divide(first_number, second_number)
                print(f"{first_number} / {second_number} = {result}")
            else:
                print("Invalid operation. Please select a valid option.")

            continue_y = input("\nDo you want to calculate something else? (yes/no): ").lower()
            if continue_y != 'yes':
                print("Exiting the calculator. Goodbye!")
                return

if __name__ == "__main__":
    main()
I have built a simple calculator program, my second task at Codsoft. The calculator supports four basic operations: Addition, Subtraction, Multiplication, and Division.



While working on this project, I learnt that giving brief informative error messages is essential to run a program smoothly and attention to detail is an important skill to have to code





#Python #Programming #Coding #PythonProjects #ModularCode #CodingProjects #Codsoft