import os

def read_file_and_count_words():
    
    filename = input("Enter the filename (with extension): ").strip()
    
    try:
        if not os.path.exists(filename):
            print(f"Error: File '{filename}' not found!")
            return
        
        # Read the file
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            
        # Count words
        words = content.split()
        word_count = len(words)
        
        # Count lines and characters
        lines = content.split('\n')
        line_count = len(lines)
        char_count = len(content)
        char_count_no_spaces = len(content.replace(' ', '').replace('\n', '').replace('\t', ''))
        
        # Display results
        print(f"\nFile Statistics for '{filename}'")
        print(f"Total words: {word_count}")
        print(f"Total lines: {line_count}")
        print(f"Total characters (including spaces): {char_count}")
        print(f"Total characters (excluding spaces): {char_count_no_spaces}")
        
        # Display first few lines as preview
        print(f"\nFile Preview (first 3 lines)")
        for i, line in enumerate(lines[:3], 1):
            print(f"Line {i}: {line}")
        
        if len(lines) > 3:
            print(f"... and {len(lines) - 3} more lines")
            
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        
    except PermissionError:
        print(f"Error: Permission denied to read file '{filename}'!")
        
    except UnicodeDecodeError:
        print(f"Error: Unable to decode file '{filename}'. It might be a binary file.")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# testing
def create_sample_file():
    sample_content = """This is a sample text file for testing the word counter program.
It contains multiple lines of text with various words.
Python is a powerful programming language.
File handling is an important concept in programming.
This program demonstrates reading files and counting words."""
    
    try:
        with open('sample.txt', 'w', encoding='utf-8') as file:
            file.write(sample_content)
        print("Sample file 'sample.txt' created successfully!")
        
    except Exception as e:
        print(f"Error creating sample file: {e}")

# Main program
if __name__ == "__main__":
    
    while True:
        print("\nOptions:")
        print("1. Read existing file and count words")
        print("2. Create sample file for testing")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            read_file_and_count_words()
            
        elif choice == '2':
            create_sample_file()
            
        elif choice == '3':
            print("Thank you for using the word counter!")
            break
            
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")