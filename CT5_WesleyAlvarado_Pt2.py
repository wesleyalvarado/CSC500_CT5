def calculate_points(num_books):
    if num_books >= 8:
        return 60
    elif num_books >= 6:
        return 30
    elif num_books >= 4:
        return 15
    elif num_books >= 2:
        return 5
    elif num_books >= 0:
        return 0
    else:
        return "Invalid input. Please enter a non-negative integer value."

def main():
    try:
        num_books = int(input("Enter the number of books purchased this month: "))
        points = calculate_points(num_books)
        if isinstance(points, int):
            print(f"You have earned {points} points.")
        else:
            print(points)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Call the main function to run the program
main()