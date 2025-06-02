class Calculator:
    
    def __init__(self):
        self.history = []
    
    def add(self, x, y):
        """Addition operation"""
        return x + y
    
    def subtract(self, x, y):
        """Subtraction operation"""
        return x - y
    
    def multiply(self, x, y):
        """Multiplication operation"""
        return x * y
    
    def divide(self, x, y):
        """Division operation with zero check"""
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return x / y

def calculator_menu():
    """Display calculator menu and handle user interactions"""
    calc = Calculator()
    
    operations = {
        '1': ('Addition', calc.add, 2),
        '2': ('Subtraction', calc.subtract, 2),
        '3': ('Multiplication', calc.multiply, 2),
        '4': ('Division', calc.divide, 2),
    }
    
    print("CALCULATOR")
    print("=" * 50)
    
    while True:
        try:
            # Display menu
            print("\nSelect an operation:")
            for key, (name, _, _) in operations.items():
                print(f"{key}. {name}")
            
            # Get user choice
            choice = input("\nEnter your choice (1-9): ").strip()
            
            if choice not in operations:
                raise ValueError("Invalid choice! Please select 1-9.")
            
            operation_name, operation_func, num_operands = operations[choice]
            
            # Get operands based on operation
            if num_operands == 1:
                num = float(input(f"Enter number for {operation_name.lower()}: "))
                result = operation_func(num)
                operation_str = f"{operation_name.lower()}({num})"
                
            elif num_operands == 2:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                result = operation_func(num1, num2)
                
                if choice == '1':
                    operation_str = f"{num1} + {num2}"
                elif choice == '2':
                    operation_str = f"{num1} - {num2}"
                elif choice == '3':
                    operation_str = f"{num1} × {num2}"
                elif choice == '4':
                    operation_str = f"{num1} ÷ {num2}"
            
            # Display result and add to history
            print(f"Result: {operation_str} = {result}")
            
        except ValueError as e:
            if "could not convert" in str(e).lower():
                print("Error: Please enter valid numbers only!")
            else:
                print(f"Value Error: {e}")
        
        except ZeroDivisionError as e:
            print(f"Division Error: {e}")
        
        except OverflowError:
            print("Error: Result is too large to calculate!")
        
        except KeyboardInterrupt:
            print("\n\nCalculator interrupted by user. Goodbye")
            break
        
        except Exception as e:
            print(f"Unexpected error occurred: {e}")
        
        print("\nPress Enter to continue or type 'quit' to exit...")
        user_input = input().strip().lower()
        if user_input == 'quit':
            print("Thank you for using the calculator! Goodbye")
            break

if __name__ == "__main__":

    calculator_menu()