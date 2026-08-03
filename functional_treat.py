"""
Project Name: Functional Treat (Data Analyzer and Transformer Program)
Author: Student
Description: A menu-driven Python program to analyze and transform 1D or 2D array data.
"""

# Global variable to store dataset summary as required in Requirement F
global_summary = {}

def update_global_summary(dataset):
    """
    Updates the global summary dictionary with basic statistics.
    Uses the global keyword to modify the global state.
    """
    global global_summary
    if not dataset:
        global_summary = {"total_elements": 0, "mean": 0}
        return
        
    global_summary = {
        "total_elements": len(dataset),
"mean": sum(dataset) / len(dataset) if dataset else 0
    }

# --- B. User-defined Functions (UDF) & G. Return Multiple Values ---
def calculate_statistics(dataset):
    """
    Calculates and returns multiple statistics about the dataset.
    Returns: (minimum, maximum, sum, average)
    """
    if not dataset:
        return 0, 0, 0, 0.0

    # A. Built-in Functions usage
    total_elements = len(dataset)
    min_val = min(dataset)
    max_val = max(dataset)
    sum_val = sum(dataset)
    avg_val = sum_val / total_elements
    
    return min_val, max_val, sum_val, avg_val

# --- C. *args, **kwargs, and __doc__ ---
def display_args_summary(*args):
    """
    Accepts multiple values using *args and displays them.
    """
    print("Values passed via *args:", ", ".join(map(str, args)))

def display_kwargs_summary(**kwargs):
    """
    Accepts key-value pairs using **kwargs to print a summary of dataset characteristics.
    """
    print("\nDataset Characteristics Summary (via **kwargs):")
    for key, value in kwargs.items():
        print(f" - {key.replace('_', ' ').title()}: {value}")

# --- D. Recursion ---
def calculate_factorial(n):
    """
    Calculates the factorial of a number using recursion.
    """
    if n == 0 or n == 1:
        return 1
    return n * calculate_factorial(n - 1)

# --- H. 1D and 2D Array formatting ---
def display_2d_grid(matrix):
    """
    Displays a 2D list in a beautifully formatted grid structure.
    """
    print("\nFormatted 2D Grid:")
    for row in matrix:
        print("\t".join(map(str, row)))

# --- Main Program Logic ---
def main():
    current_data = [] # Stores our active dataset (1D or 2D)
    is_2d = False

    while True:
        # Menu-driven Interface
        print("\n" + "="*50)
        print("Welcome to the Data Analyzer and Transformer Program")
        print("="*50)
        print("Main Menu:")
        print("1. Input Data")
        print("2. Display Data Summary (Built-in Functions)")
        print("3. Calculate Factorial (Recursion)")
        print("4. Filter Data by Threshold (Lambda Function)")
        print("5. Sort Data")
        print("6. Display Dataset Statistics (Return Multiple Values)")
        print("0. Exit Program")
        print("="*50)
        
        try:
            choice = int(input("Please enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 7.")
            continue

        if choice == 1:
                print("\n--- Step 1: Input Data ---")
                raw_input = input("Enter data for a 1D array (separated by spaces):\n")
                current_data = [int(x) for x in raw_input.split()]
                is_2d = False
                print("\nData has been stored successfully!")

        elif choice == 2:
            print("\n--- Step 2: Display Data Summary (Built-in Functions) ---")
            # Docstring print demo as required
            print(f"Function Documentation: {calculate_statistics.__doc__.strip()}")
            
            if not current_data:
                print("No data available! Please input data first.")
                continue
                
            min_v, max_v, sum_v, avg_v = calculate_statistics(current_data)
            
            # Flattening count for exact display
            total_elements = global_summary.get("total_elements", 0)
            
            print("\nData Summary:")
            print(f" - Total elements: {total_elements}")
            print(f" - Minimum value: {min_v}")
            print(f" - Maximum value: {max_v}")
            print(f" - Sum of all values: {sum_v}")
            print(f" - Average value: {avg_v:.2f}")

        elif choice == 3:
            print("\n--- Step 3: Calculate Factorial (Recursion) ---")
            print(f"Function Documentation: {calculate_factorial.__doc__.strip()}")
            try:
                num = int(input("Enter a number to calculate its factorial: "))
                if num < 0:
                    print("Factorial is not defined for negative numbers.")
                else:
                    print(f"\nFactorial of {num} is: {calculate_factorial(num)}")
            except ValueError:
                print("Please enter a valid integer.")

        elif choice == 4:
            print("\n--- Step 4: Filter Data by Threshold (Lambda Function) ---")
            if not current_data:
                print("No data available! Please input data first.")
                continue
                
            try:
                threshold = int(input("Enter a threshold value to filter out data above this value: "))
                
                # Flatten the data if 2D for easier lambda processing
                flat_list = []
                if is_2d:
                    for row in current_data: flat_list.extend(row)
                else:
                    flat_list = current_data
                
                # E. Lambda with filter() to filter items >= threshold
                filtered_result = list(filter(lambda x: x >= threshold, flat_list))
                
                print(f"\nFiltered Data (values >= {threshold}):")
                print(", ".join(map(str, filtered_result)))
            except ValueError:
                print("Invalid input threshold.")

        elif choice == 5:
            print("\n--- Step 5: Sort Data ---")
            if not current_data:
                print("No data available!")
                continue
                
            print("Choose sorting option:\n1. Ascending\n2. Descending")
            sort_choice = input("Enter your choice: ")
            reverse_order = True if sort_choice == '2' else False
            
            if not is_2d:
                # I. In-place sorting using sort() method on 1D list
                sorted_data = current_data.copy()
                sorted_data.sort(reverse=reverse_order)
                order_txt = "Descending" if reverse_order else "Ascending"
                print(f"\nSorted Data in {order_txt} Order:")
                print(", ".join(map(str, sorted_data)))
            else:
                # I. Using sorted() function to sort rows inside 2D list without changing original
                print("\nSorting each row inside the 2D array:")
                new_sorted_2d = [sorted(row, reverse=reverse_order) for row in current_data]
                display_2d_grid(new_sorted_2d)

        elif choice == 6:
            print("\n--- Step 6: Display Dataset Statistics (Return Multiple Values) ---")
            if not current_data:
                print("No data available!")
                continue
                
            min_v, max_v, sum_v, avg_v = calculate_statistics(current_data)
            
            # Triggering kwargs demonstration
            display_kwargs_summary(
                minimum_value=min_v,
                maximum_value=max_v,
                sum_of_values=sum_v,
                average_value=round(avg_v, 2),
                global_tracked_mean=round(global_summary.get("mean", 0), 2)
            )

        elif choice == 0:
            print("\n--- Step 7: Exit Program ---")
            print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
            break
            
        else:
            print("Invalid Option! Please select from 1 to 7.")

if __name__ == "__main__":
    main()