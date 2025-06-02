def main():
    students = {}
    
    while True:
        print("\n</ Student Score Tracker />")
        print("1. Input student names and scores")
        print("2. Calculate statistics")
        print("3. Save data to file")
        print("4. Exit")
        
        try:
            choice = input("Enter your choice (1-4): ")
            
            if choice == '1':
                input_student_data(students)
            elif choice == '2':
                calculate_statistics(students)
            elif choice == '3':
                save_to_file(students)
            elif choice == '4':
                print("Goodbye")
                break
            else:
                print("Invalid choice. Please enter 1-4.")
                
        except Exception as e:
            print(f"Error: {e}")

def input_student_data(students):
    try:
        name = input("Enter student name: ").strip()
        if not name:
            print("Error: Name cannot be empty.")
            return
            
        score = float(input("Enter student score: "))
        if score < 0 or score > 100:
            print("Error: Score must be between 0 and 100.")
            return
            
        students[name] = score
        print(f"Added {name} with score {score}")
        
    except ValueError:
        print("Error: Please enter a valid number for the score.")

def calculate_statistics(students):
    if not students:
        print("No student data available.")
        return
    
    scores = list(students.values())
    average = sum(scores) / len(scores)
    highest = max(scores)
    lowest = min(scores)
    
    print(f"\n=== Statistics ===")
    print(f"Average score: {average:.2f}")
    print(f"Highest score: {highest}")
    print(f"Lowest score: {lowest}")
    
    for name, score in students.items():
        if score == highest:
            print(f"Highest scorer: {name}")
        if score == lowest:
            print(f"Lowest scorer: {name}")

def save_to_file(students):
    if not students:
        print("No student data to save.")
        return
    
    try:
        filename = "student_scores.txt"
        with open(filename, 'w') as file:
            file.write("Student Score Report\n")
            
            for name, score in students.items():
                file.write(f"{name}: {score}\n")
            
            # Add statistics to file
            scores = list(students.values())
            average = sum(scores) / len(scores)
            highest = max(scores)
            lowest = min(scores)
            
            file.write(f"\nStatistics:\n")
            file.write(f"Average: {average:.2f}\n")
            file.write(f"Highest: {highest}\n")
            file.write(f"Lowest: {lowest}\n")
        
        print(f"Data saved to {filename}")
        
    except Exception as e:
        print(f"Error saving file: {e}")

if __name__ == "__main__":
    main()