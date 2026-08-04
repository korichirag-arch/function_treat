# =========================================================
# Project: Functional Treat - Data Analyzer and Transformer
# Focus: 1D Array (List) Operations
# =========================================================

global_summary = {}

# --- Built-in Functions ---
def display_builtin_summary(data):
    """Calculates basic statistics using built-in functions."""
    if not data:
        print("\nData Summary:")
        print("Dataset is empty! Please input data first.")
        return

    print("\nData Summary:")
    print(f"- Total elements: {len(data)}")
    print(f"- Minimum value: {min(data)}")
    print(f"- Maximum value: {max(data)}")
    print(f"- Sum of all values: {sum(data)}")

# --- User-Defined Functions ---
def display_udf_summary(data):
    """Calculates average and displays unique values."""
    if not data:
        print("\nDataset is empty!")
        return
    
    avg = sum(data) / len(data)
    uniques = list(set(data))
    print(f"\nAverage Value: {avg:.2f}")
    print(f"Unique Values: {uniques}")

# --- Recursion ---
def calculate_factorial(n):
    """Recursively calculates factorial."""
    if n <= 1:
        return 1
    return n * calculate_factorial(n - 1)

# --- Lambda, map, filter ---
def filter_data_by_threshold(data):
    """Filters data using lambda function."""
    if not data:
        print("\nDataset is empty!")
        return
    try:
        threshold = float(input("\nEnter threshold value: "))
        filtered = list(filter(lambda x: x > threshold, data))
        print(f"Filtered Values (greater than {threshold}): {filtered}")
    except ValueError:
        print("Invalid threshold input!")

# --- Return Multiple Values ---
def get_dataset_stats(data):
    """Returns multiple statistics from dataset."""
    if not data:
        return 0, 0, 0
    return min(data), max(data), sum(data) / len(data)

# --- *args and **kwargs ---
def display_kwargs_summary(**kwargs):
    """Prints dataset summary using **kwargs."""
    print("\nDataset Characteristics Summary:")
    for key, value in kwargs.items():
        print(f"- {key}: {value}")

# --- Global Keyword ---
def update_global_stats(data):
    """Updates global summary variables."""
    global global_summary
    if data:
        global_summary = {
            "Total Elements": len(data),
            "Overall Mean": sum(data) / len(data)
        }

# --- Sorting ---
def sort_data(data):
    """Sorts 1D list using sort() and sorted()."""
    if not data:
        print("\nDataset is empty!")
        return
    
    # Demonstration of in-place sort
    sorted_copy = sorted(data)
    print(f"\nSorted Data: {sorted_copy}")


# =========================================================
# Main Menu Interface (Matching Console Output Exact)
# =========================================================
def main():
    dataset = []

    while True:
        print("\nWelcome to the Data Analyzer and Transformer Program\n")
        print("Main Menu:")
        print("1. Input Data")
        print("2. Display Data Summary (Built-in Functions)")
        print("3. Calculate Factorial (Recursion)")
        print("4. Filter Data by Threshold (Lambda Function)")
        print("5. Sort Data")
        print("6. Display Dataset Statistics (Return Multiple Values)")
        print("7. Exit Program")

        choice = input("Please enter your choice: ").strip()

        # Step 1: Input Data (Exact line input as shown in screenshot)
        if choice == '1':
            print("\nStep 1: Input Data")
            print("Please enter your choice: 1\n")
            raw_input = input("Enter data for a 1D array (separated by spaces):\n")
            
            try:
                # Direct single line split space separated numbers
                dataset = [int(x) for x in raw_input.strip().split()]
                print("\nData has been stored successfully!")
                update_global_stats(dataset)
            except ValueError:
                print("\nInvalid input! Please enter space-separated numbers.")

        # Step 2: Display Summary
        elif choice == '2':
            print("\nStep 2: Display Data Summary (Built-in Functions)")
            print("Please enter your choice: 2")
            display_builtin_summary(dataset)

        # Step 3: Recursion
        elif choice == '3':
            try:
                num = int(input("\nEnter integer for Factorial calculation: "))
                print(f"Factorial of {num} is: {calculate_factorial(num)}")
            except ValueError:
                print("Invalid number!")

        # Step 4: Filter Data
        elif choice == '4':
            filter_data_by_threshold(dataset)

        # Step 5: Sort Data
        elif choice == '5':
            sort_data(dataset)

        # Step 6: Return Multiple Values
        elif choice == '6':
            if dataset:
                min_v, max_v, avg_v = get_dataset_stats(dataset)
                print(f"\nStatistics -> Min: {min_v}, Max: {max_v}, Average: {avg_v:.2f}")
                # kwarg usage demonstration
                display_kwargs_summary(Total_Elements=len(dataset), Mean=avg_v)
            else:
                print("\nDataset is empty!")

        # Step 7: Exit
        elif choice == '7':
            print("\nExiting program...")
            break
        else:
            print("\nInvalid choice! Please select 1-7.")

if __name__ == "__main__":
    main()
    
