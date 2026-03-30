def calculator():
    print("SMART CALCULATOR")
    print("Operations: +, -, *, /")
    
    while True:
        try:
            # User input
            num1 = float(input("\nEnter first number: "))
            operation = input("Enter operation (+, -, *, /): ")
            num2 = float(input("Enter second number: "))
            
            # Calculations
            if operation == '+':
                result = num1 + num2
                print(f"{num1} + {num2} = {result}")
            elif operation == '-':
                result = num1 - num2
                print(f"{num1} - {num2} = {result}")
            elif operation == '*':
                result = num1 * num2
                print(f"{num1} * {num2} = {result}")
            elif operation == '/':
                if num2 == 0:
                    print("Error: Cannot divide by zero!")
                    continue
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
            else:
                print("Invalid operation! Use +, -, *, /")
                continue
                
        except ValueError:
            print("Please enter valid numbers!")
            continue
        
        # Repeat option
        repeat = input("\nCalculate again? (y/n): ").lower()
        if repeat != 'y':
            print("Thanks for using Smart Calculator!")
            break

# Run calculator
calculator()