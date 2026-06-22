# Simple Python Calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def show_menu():
    print("\n" + "="*40)
    print("      🧮  Simple Calculator")
    print("="*40)
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("="*40)

# Main program loop
while True:
    show_menu()
    
    # Choose operation
    try:
        choice = input("Choose operation (1-5): ")
        
        if choice == '5':
            print("👋 Goodbye!")
            break
        
        if choice not in ['1', '2', '3', '4']:
            print("❌ Invalid choice! Please choose a number from 1 to 4")
            continue
        
        # Input numbers
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("❌ Error: Please enter valid numbers!")
            continue
        
        # Perform operation
        if choice == '1':
            result = add(num1, num2)
            operation = "+"
        elif choice == '2':
            result = subtract(num1, num2)
            operation = "-"
        elif choice == '3':
            result = multiply(num1, num2)
            operation = "×"
        elif choice == '4':
            result = divide(num1, num2)
            operation = "÷"
        
        # Display result
        print(f"\n✅ {num1} {operation} {num2} = {result}")
        print("-"*40)
        
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
        break
    except Exception as e:
        print(f"❌ An error occurred: {e}")