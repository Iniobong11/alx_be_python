# finance_calculator.py

# Prompt the user for financial details
income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = income - expenses

# Project annual savings with 5% interest (explicit formula)
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)

# Format numbers so whole floats print without .0
def fmt_number(n):
    # if n is a float and has no fractional part, print as int
    if isinstance(n, float) and n.is_integer():
        return str(int(n))
    return str(n)

# Output results (matching the expected phrasing)
print("Your monthly savings are $", fmt_number(monthly_savings), ".", sep="")
print("Projected savings after one year, with interest, is: $", fmt_number(projected_savings), ".", sep="")
