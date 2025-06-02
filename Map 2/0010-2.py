import pandas as pd
import numpy as np
import os

def create_sample_dataset():
    """Create a sample dataset """
    
    # Sample student data
    data = {
        'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Name': ['A', 'B', 'C', 'D', 'E', 
                'F', 'G', 'H', 'I', 'J'],
        'Age': [20, 21, 19, 22, 20, 23, 19, 21, 20, 22],
        'Grade': ['A', 'B', 'B+', 'A-', 'B', 'C+', 'A', 'B-', 'A-', 'B+'],
        'Math_Score': [95, 78, 85, 92, 76, 68, 98, 73, 89, 82],
        'Science_Score': [88, 82, 79, 94, 71, 65, 96, 69, 91, 85],
        'English_Score': [92, 75, 88, 89, 82, 72, 94, 78, 87, 80],
        'City': ['new', 'ampara', 'town', 'comolbo', 'galle',
                'jaffna', 'mulathiv', 'anuradhapura', 'polonnaruwa', 'sigiriya']
    }
    
    df = pd.DataFrame(data)
    df.to_csv('student_data.csv', index=False)
    print("Sample dataset 'student_data.csv' created successfully!")
    return df

def explore_dataset(df):
    #Comprehensive dataset exploration
    
    print("\nDataset Exploration")
    
    # Basic information
    print("\n1. Dataset Shape and Info:")
    print(f"Dataset shape: {df.shape}")
    print(f"Number of rows: {df.shape[0]}")
    print(f"Number of columns: {df.shape[1]}")
    print(f"Column names: {list(df.columns)}")
    
    print("\n2. Dataset Info:")
    print(df.info())
    
    print("\n3. First 5 rows:")
    print(df.head())
    
    print("\n4. Last 5 rows:")
    print(df.tail())
    
    # Data types
    print("\n6. Data Types:")
    print(df.dtypes)
    
    # Missing values
    print("\n7. Missing Values:")
    missing_values = df.isnull().sum()
    print(missing_values)
    if missing_values.sum() == 0:
        print("No missing values found!")
    
    # Unique values
    print("\n8. Unique Values in Categorical Columns:")
    categorical_columns = df.select_dtypes(include=['object']).columns
    for col in categorical_columns:
        print(f"{col}: {df[col].nunique()} unique values")
        print(f"Values: {df[col].unique()}")
        print()
    
    # Basic analysis
    print("\n9. Basic Analysis:")
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    
    for col in numeric_columns:
        if col != 'Student_ID':
            print(f"\n{col}:")
            print(f"  Mean: {df[col].mean():.2f}")
            print(f"  Median: {df[col].median():.2f}")
            print(f"  Min: {df[col].min()}")
            print(f"  Max: {df[col].max()}")
            print(f"  Standard Deviation: {df[col].std():.2f}")

def data_filtering_operations(df):
    
    print("\nData Filtering and Manipulation")
    
    # Filtering operations
    print("\n1. Filtering Operations:")
    
    # Students with high math scores
    high_math = df[df['Math_Score'] >= 85]
    print(f"Students with Math Score >= 85:")
    print(high_math[['Name', 'Math_Score']])
    
    # Students from specific cities
    print(f"\nStudents from New York or galle:")
    city_filter = df[df['City'].isin(['galle', 'colombo'])]
    print(city_filter[['Name', 'City']])
    
    # Multiple conditions
    print(f"\nStudents with Age > 20 AND Math Score > 80:")
    complex_filter = df[(df['Age'] > 20) & (df['Math_Score'] > 80)]
    print(complex_filter[['Name', 'Age', 'Math_Score']])
    
    print("\n2. Sorting Operations:")
    
    # Sort by math score
    sorted_by_math = df.sort_values('Math_Score', ascending=False)
    print("Top 5 students by Math Score:")
    print(sorted_by_math[['Name', 'Math_Score']].head())
    
    print("\n3. Grouping Operations:")
    
    # Group by grade
    grade_stats = df.groupby('Grade').agg({
        'Math_Score': ['mean', 'min', 'max'],
        'Science_Score': ['mean', 'min', 'max'],
        'English_Score': ['mean', 'min', 'max']
    }).round(2)
    print("Statistics by Grade:")
    print(grade_stats)
    
    print("\n4. New Column Creation:")
    
    # Calculate average score
    df_copy = df.copy()
    df_copy['Average_Score'] = (df_copy['Math_Score'] + 
                               df_copy['Science_Score'] + 
                               df_copy['English_Score']) / 3
    
    print("Students with their Average Scores:")
    print(df_copy[['Name', 'Math_Score', 'Science_Score', 
                   'English_Score', 'Average_Score']].round(2))

def load_custom_dataset():
    filename = input("Enter the CSV filename (with extension): ").strip()
    
    try:
        if not os.path.exists(filename):
            print(f"File '{filename}' not found!")
            return None
            
        df = pd.read_csv(filename)
        print(f"Dataset '{filename}' loaded successfully!")
        return df
        
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

if __name__ == "__main__":
    print("Pandas is required for this program.")
    print("Install it using: pip install pandas\n")
    
    try:
        while True:
            print("1. Create and explore sample dataset")
            print("2. Load and explore custom CSV file")
            print("3. Exit")
            
            choice = input("Enter your choice (1-3): ").strip()
            
            if choice == '1':
                # Create sample dataset
                df = create_sample_dataset()
                
                while True:
                    print("\nSample Dataset Options:")
                    print("1. Basic exploration")
                    print("2. Data filtering and manipulation")
                    print("3. Back to main menu")
                    
                    sub_choice = input("Enter your choice (1-3): ").strip()
                    
                    if sub_choice == '1':
                        explore_dataset(df)
                    elif sub_choice == '2':
                        data_filtering_operations(df)
                    elif sub_choice == '3':
                        break
                    else:
                        print("Invalid choice!")
                
            elif choice == '2':
                df = load_custom_dataset()
                if df is not None:
                    while True:
                        print("\nCustom Dataset Options:")
                        print("1. Basic exploration")
                        print("2. Data filtering (if applicable)")
                        print("3. Back to main menu")
                        
                        sub_choice = input("Enter your choice (1-3): ").strip()
                        
                        if sub_choice == '1':
                            explore_dataset(df)
                        elif sub_choice == '2':
                            try:
                                data_filtering_operations(df)
                            except Exception as e:
                                print(f"Error in data filtering: {e}")
                                print("This might be due to incompatible data structure.")
                        elif sub_choice == '3':
                            break
                        else:
                            print("Invalid choice!")
                
            elif choice == '3':
                print("Thank you for using Pandas Dataset Explorer!")
                break
                
            else:
                print("Invalid choice!")
                
    except ImportError:
        print("Error: Pandas is not installed!")
        print("Please install Pandas using: pip install pandas")