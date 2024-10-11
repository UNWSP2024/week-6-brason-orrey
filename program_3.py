STATE_TAX_RATE = 0.05
COUNTY_TAX_RATE = 0.025

def calculate_tax(sales_amount):
    county_tax = sales_amount * COUNTY_TAX_RATE
    state_tax = sales_amount * STATE_TAX_RATE
    total_tax = county_tax + state_tax
    return county_tax, state_tax, total_tax

def main():
    total_sales = float(input("Enter the total sales for the month: $"))
    
    county_tax, state_tax, total_tax = calculate_tax(total_sales)
    
    # Display the results
    print(f"County sales tax: ${county_tax:.2f}")
    print(f"State sales tax: ${state_tax:.2f}")
    print(f"Total sales tax: ${total_tax:.2f}")

main()
