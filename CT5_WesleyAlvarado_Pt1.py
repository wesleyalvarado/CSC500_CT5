
import calendar

def rainfall_statistics():
    # Ask the user the number of years of rainfall data
    num_years = int(input("Enter the number of years of rainfall data: "))

    total_rainfall = 0  # Accumulate the total rainfall volume over all years

    # Outer loop for each year of rainfall data
    for year in range(1, num_years + 1):
        # Inner loop for each month of rainfall data
        for month in range(1, 13):
            #We can use the Calendar library to display the month name when prompting the user for rainfall data
            rainfall = float(input(f"Enter the inches of rainfall for {calendar.month_name[month]} Year {year} : "))
            total_rainfall += rainfall

    # Calculate the total number of months2
    total_months = num_years * 12

    # Calculate the average rainfall per month
    average_rainfall = total_rainfall / total_months

    # Display the results
    print("\n---Rainfall data results---")
    print(f"Total Number of months: {total_months}")
    print(f"Total inches of rainfall: {total_rainfall}")
    print(f"Average rainfall per month for all years: {average_rainfall:.2f} inches")

# Calls the main function to run the program
rainfall_statistics()