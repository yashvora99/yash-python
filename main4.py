def display_menu():
    print("\nWelcome to the Data Analyzer and Transformer Program")
    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")

def input_data():
    global data
    data_input = input("\nEnter data for a 1D array (separated by spaces): ")
    data = list(map(int, data_input.strip().split()))
    print("\nData has been stored successfully!")

def display_summary():
    print("\nData Summary:")
    print(f"- Total elements: {len(data)}")
    print(f"- Minimum value: {min(data)}")
    print(f"- Maximum value: {max(data)}")
    print(f"- Sum of all values: {sum(data)}")
    print(f"- Average value: {round(sum(data)/len(data), 2)}")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def calculate_factorial():
    num = int(input("\nEnter a number to calculate its factorial: "))
    print(f"\nFactorial of {num} is: {factorial(num)}")

def filter_data():
    threshold = int(input("\nEnter a threshold value to filter out data below this value: "))
    filtered = list(filter(lambda x: x >= threshold, data))
    print(f"\nFiltered Data (values >= {threshold}):")
    print(*filtered)

def sort_data():
    print("\nChoose sorting option:")
    print("1. Ascending")
    print("2. Descending")
    choice = input("\nEnter your choice: ")
    if choice == "1":
        sorted_data = sorted(data)
        print("\nSorted Data in Ascending Order:")
    else:
        sorted_data = sorted(data, reverse=True)
        print("\nSorted Data in Descending Order:")
    print(*sorted_data)

def dataset_statistics():
    min_val = min(data)
    max_val = max(data)
    total = sum(data)
    average = round(total / len(data), 2)
    print("\nDataset Statistics:")
    print(f"- Minimum value: {min_val}")
    print(f"- Maximum value: {max_val}")
    print(f"- Sum of all values: {total}")
    print(f"- Average value: {average}")

# Main program
data = []
while True:
    display_menu()
    choice = input("\nPlease enter your choice: ")

    if choice == "1":
        input_data()
    elif choice == "2":
        display_summary()
    elif choice == "3":
        calculate_factorial()
    elif choice == "4":
        filter_data()
    elif choice == "5":
        sort_data()
    elif choice == "6":
        dataset_statistics()
    elif choice == "7":
        print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye!")
        break
    else:
        print("\nInvalid choice! Please try again.")