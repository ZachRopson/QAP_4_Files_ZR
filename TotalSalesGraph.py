# Program to graph the total sales by month for our insurance claim company
# Written by: Zachary Ropson
# Date Written: November 26- November 27, 2023

import matplotlib.pyplot as plt

def create_sales_graph(months, total_sales):
    # Create a bar graph
    plt.bar(months, total_sales, color='blue')

    # Add title and labels for months and sales
    plt.title('Total Sales ($) by Month')
    plt.xlabel('Months')
    plt.ylabel('Total Sales ($)')

    # Display the graph
    plt.show()

def main():
    # List to store total sales for each month
    total_sales = []

    # List of months
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    # Get total sales for each month from the user
    for month in months:
        while True:
            try:
                sales = float(input(f"Enter total sales for {month}: $"))
                total_sales.append(sales)
                break
            except ValueError:
                print("Invalid input. Please enter a valid numeric value for total sales.")

    # Create and display the sales graph
    create_sales_graph(months, total_sales)

if __name__ == "__main__":
    main()
