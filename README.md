# One Stop Insurance Management System

## Description

The One Stop Insurance Management System is a Python program designed for the One Stop Insurance Company to efficiently enter and calculate new insurance policy information for its customers. The program allows the user to input customer details, insurance options, and payment information, and it calculates the insurance premium based on specified rates and options. The generated receipt includes all input values, calculated costs, and a summary of the insurance policy.

## Features

- User-friendly, readable code
- Input validation for provinces, payment methods, and numeric values.
- Calculation of insurance premium based on specified rates and options.
- Generation of detailed receipts including customer information, insurance details, payment information, and previous claims.
- Support for numerous customers with continuous data entry and incremental policy numbers.

## Functions

1. **validate_province(province):**
   - Validates the input province against a list of valid province codes.

2. **calculate_premium(num_cars, extra_liability, glass_coverage, loaner_car):**
   - Calculates the total insurance premium based on the number of cars and selected insurance options.

3. **generate_receipt(customer_info, policy_number, payment_method, down_payment=None):**
   - Generates a detailed receipt including customer information, insurance details, payment information, and previous claims.
