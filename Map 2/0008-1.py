def division_with_error_handling():
    
    while True:
        try:
            # Get input from user
            print("\nEnter two numbers for division (or 'quit' to exit):")
            
            numerator_input = input("Enter numerator: ")
            if numerator_input.lower() == 'quit':
                print("Goodbye!")
                break
                
            denominator_input = input("Enter denominator: ")
            if denominator_input.lower() == 'quit':
                print("Goodbye!")
                break
            
            # Convert to float
            numerator = float(numerator_input)
            denominator = float(denominator_input)
            
            # Perform division
            result = numerator / denominator
            print(f"Result: {numerator} ÷ {denominator} = {result}")
            
        except ZeroDivisionError:
            print("Error: Cannot divide by zero!!! Please enter a non-zero denominator.")
            
        except ValueError:
            print("Error: Please enter valid numbers only")
            
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Goodbye")
            break
            
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
        # Asking if user wants to continue
        continue_choice = input("\nDo you want to perform another division? (y/n): ")
        if continue_choice.lower() != 'y':
            print("Goodbye!")
            break

# Test
def test_division_examples():  
    test_cases = [
        (10, 2),    
        (15, 3),   
        (0, 5),    
        (-10, 2),   
    ]
    
    for num, den in test_cases:
        try:
            result = num / den
            print(f"{num} ÷ {den} = {result}")
        except ZeroDivisionError:
            print(f"{num} ÷ {den} = Error: Division by zero")
        except Exception as e:
            print(f"{num} ÷ {den} = Error: {e}")

if __name__ == "__main__":
    division_with_error_handling()
    
    test_division_examples()