import datetime
import os

class SimpleLogger:
    def __init__(self, log_filename="application.log"):
        self.log_filename = log_filename
        self.ensure_log_file_exists()
    
    def ensure_log_file_exists(self):
        if not os.path.exists(self.log_filename):
            try:
                with open(self.log_filename, 'w', encoding='utf-8') as file:
                    file.write(f"Log File Created on {datetime.datetime.now()}\n")
                print(f"Log file '{self.log_filename}' created.")
            except Exception as e:
                print(f"Error creating log file: {e}")
    
    def write_log(self, message, log_level="INFO"):
        try:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"[{timestamp}] {log_level}: {message}\n"
            
            # Append to log file
            with open(self.log_filename, 'a', encoding='utf-8') as file:
                file.write(log_entry)
            
            print(f"Log entry added: [{log_level}] {message}")
            
        except Exception as e:
            print(f"Error writing to log file: {e}")
    
    def read_logs(self):
        try:
            if not os.path.exists(self.log_filename):
                print("No log file found!")
                return
            
            with open(self.log_filename, 'r', encoding='utf-8') as file:
                logs = file.read()
            
            if logs.strip():
                print(f"\nContents of {self.log_filename}")
                print(logs)
            else:
                print("Log file is empty.")
                
        except Exception as e:
            print(f"Error reading log file: {e}")
    
    def clear_logs(self):
        try:
            with open(self.log_filename, 'w', encoding='utf-8') as file:
                file.write(f"Log File Cleared on {datetime.datetime.now()}\n")
            print("Log file cleared successfully")
            
        except Exception as e:
            print(f"Error clearing log file: {e}")

def demonstrate_logging():
    logger = SimpleLogger()
    
    # Sample 
    logger.write_log("Application started", "INFO")
    logger.write_log("User logged in successfully", "INFO")
    logger.write_log("Database connection established", "INFO")
    logger.write_log("Invalid input received", "WARNING")
    logger.write_log("File not found", "ERROR")
    logger.write_log("Application shutting down", "INFO")

if __name__ == "__main__":
    print("Simple Log System")
    logger = SimpleLogger()
    
    while True:
        print("\nOptions:")
        print("1. Write a log message")
        print("2. View all logs")
        print("3. Clear all logs")
        print("4. Run demonstration")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            message = input("Enter log message: ").strip()
            if message:
                print("Log levels: INFO, WARNING, ERROR")
                level = input("Enter log level (default: INFO): ").strip().upper()
                if level not in ["INFO", "WARNING", "ERROR"]:
                    level = "INFO"
                logger.write_log(message, level)
            else:
                print("Message cannot be empty!")
        
        elif choice == '2':
            logger.read_logs()
        
        elif choice == '3':
            confirm = input("Are you sure you want to clear all logs? (y/n): ").lower()
            if confirm == 'y':
                logger.clear_logs()
        
        elif choice == '4':
            demonstrate_logging()
            
        elif choice == '5':
            print("Thank you for using the log system!")
            break
            
        else:
            print("Invalid choice. Please enter 1-5.")