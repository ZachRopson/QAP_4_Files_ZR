#      program to enter and calculate new 
# insurance policy information for its customers
# Written By: Zachary Ropson
# Date Written: November 23rd - November 27, 2023

from datetime import datetime, timedelta

#Default Values
next_policy_number = 1944
basic_premium = 869.00
discount_for_additional_cars = 0.25
cost_of_extra_liability = 130.00
cost_of_glass_coverage = 86.00
cost_for_loaner_car_coverage = 58.00
hst_rate = 0.15
processing_fee = 39.99

# Lists to store claims
claim_dates = []
claim_amounts = []

# Function to validate province
def validate_province(province):
    provinces = ['ON', 'QC', 'BC', 'AB', 'MB', 'SK', 'NS', 'NB', 'NL', 'PE', 'NT', 'YT', 'NU']
    return province.upper() in provinces

# Function to calculate premium
def calculate_premium(num_cars, extra_liability, glass_coverage, loaner_car):
    total_extra_costs = num_cars * (extra_liability + cost_of_glass_coverage + cost_for_loaner_car_coverage * loaner_car)
    total_premium = basic_premium + (num_cars - 1) * basic_premium * discount_for_additional_cars + total_extra_costs
    total_hst = total_premium * hst_rate
    total_cost = total_premium + total_hst
    return total_cost, total_extra_costs, total_hst

    # Function to generate receipt
def generate_receipt(customer_info, policy_number, payment_method, down_payment=None):
    receipt_date = datetime.now().strftime("%Y-%m-%d")
    invoice_date = receipt_date
    first_payment_date = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")

    receipt = f"{'='*30}\n{'One Stop Insurance Receipt':^30}\n{'='*30}\n"
    receipt += f"Policy Number: {policy_number}\n"
    receipt += f"{'='*30}\n{'Customer Information':^30}\n{'='*30}\n"
    receipt += f"First Name: {customer_info['First Name']}\n"
    receipt += f"Last Name: {customer_info['Last Name']}\n"
    receipt += f"Address: {customer_info['Address']}\n"
    receipt += f"City: {customer_info['City']}\n"
    receipt += f"Province: {customer_info['Province']}\n"
    receipt += f"Postal Code: {customer_info['Postal Code']}\n"
    receipt += f"Phone Number: {customer_info['Phone Number']}\n"
    receipt += f"{'='*30}\n{'Insurance Details':^30}\n{'='*30}\n"
    receipt += f"Number of Cars Insured: {num_cars}\n"
    receipt += f"Extra Liability: {'Yes' if extra_liability else 'No'}\n"
    receipt += f"Glass Coverage: {'Yes' if glass_coverage else 'No'}\n"
    receipt += f"Loaner Car Option: {'Yes' if loaner_car else 'No'}\n"
    receipt += f"{'='*30}\n{'Payment Details':^30}\n{'='*30}\n"
    receipt += f"Payment Method: {payment_method}\n"
    if payment_method.lower() == 'down pay':
        receipt += f"Down Payment: ${down_payment:.2f}\n"
    receipt += f"{'='*30}\n{'Invoice Details':^30}\n{'='*30}\n"
    receipt += f"Receipt Date: {receipt_date}\n"
    receipt += f"Invoice Date: {invoice_date}\n"
    receipt += f"First Payment Date: {first_payment_date}\n"
    receipt += f"{'='*30}\n{'Total Cost':^30}\n{'='*30}\n"
    receipt += f"Basic Premium: ${basic_premium:.2f}\n"
    receipt += f"Extra Costs: ${total_extra_costs:.2f}\n"
    receipt += f"HST: ${total_hst:.2f}\n"
    receipt += f"Processing Fee: ${processing_fee:.2f}\n"
    receipt += f"{'='*30}\nTotal Cost: ${total_cost:.2f}\n"
    receipt += f"{'='*30}\n{'Previous Claims':^30}\n{'='*30}\n"
    receipt += "Claim #  Claim Date   Amount\n"
    receipt += "-" * 30 + "\n"
    for i, (claim_date, claim_amount) in enumerate(zip(claim_dates, claim_amounts), start=1):
        receipt += f"{i}.".ljust(7) + f"{claim_date}".ljust(15) + f"${claim_amount:.2f}\n"

    print(receipt)


# Main program for insurance claim
while True:
    # Get customer information for user input
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    address = input("Enter address: ")
    city = input("Enter city: ").title()
    province = input("Enter province (2 characters): ").upper()
    while not validate_province(province):
        province = input("Invalid province. Enter a valid 2-character province code: ").upper()
    postal_code = input("Enter postal code: ")
    phone_number = input("Enter phone number: ")

    # Get insurance details
    num_cars = int(input("Enter number of cars being insured: "))

    # Allow the user to input extra liability coverage up to $1,000,000
    while True:
        try:
            extra_liability_input = input("Enter extra liability coverage amount (in dollars) or press Enter for default: ")
            if not extra_liability_input:
                extra_liability = 0
                break
            extra_liability = float(extra_liability_input)
            if 0 <= extra_liability <= 1000000:
                break
            else:
                print("Invalid input. Extra liability coverage must be between 0 and $1,000,000.")
        except ValueError:
            print("Invalid input. Please enter a valid numeric value for extra liability coverage.")

    glass_coverage = input("Glass coverage? (Y/N): ").upper() == 'Y'
    loaner_car = input("Loaner car coverage? (Y/N): ").upper() == 'Y'

    # Get payment details with validation
    while True:
        payment_method = input("Payment method (Full/Monthly/Down Pay): ").title()
        if payment_method in ['Full', 'Monthly', 'Down Pay']:
            break
        else:
            print("Invalid payment method. Please enter Full, Monthly, or Down Pay.")

    # If Down Pay is selected, allow user to enter the down payment amount
    down_payment = None
    if payment_method == 'Down Pay':
        while True:
            try:
                down_payment = float(input("Enter down payment amount: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid numeric value for the down payment.")

    # Get and store previous claims
    while True:
        claim_date = input("Enter claim date (YYYY-MM-DD, press Enter to finish): ")
        if not claim_date:
            break
        try:
            claim_amount = float(input("Enter claim amount: "))
        except ValueError:
            print("Invalid input. Please enter a valid numeric value for the claim amount.")
            continue
        claim_dates.append(claim_date)
        claim_amounts.append(claim_amount)

    # Calculate premium
    total_cost, total_extra_costs, total_hst = calculate_premium(num_cars, extra_liability, glass_coverage, loaner_car)



    # Generate and display receipt
    generate_receipt(
        {"First Name": first_name, "Last Name": last_name, "Address": address, "City": city,
         "Province": province, "Postal Code": postal_code, "Phone Number": phone_number},
        next_policy_number, payment_method, down_payment
    )

    # Increment policy number for the next customer
    next_policy_number += 1

    # Ask the user if they want to enter another customer
    another_customer = input("Do you want to enter another customer? (Y/N): ").upper()
    if another_customer != 'Y':
        break


