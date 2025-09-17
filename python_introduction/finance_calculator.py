# finance_calculator.py

# Prompt the user for financial details
income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = income - expenses

# Project annual savings with 5% interest (explicit formula)
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

# Output results
print("Your monthly savings are $", monthly_savings, ".", sep="")
print("Projected savings after one year, with interest, is: $", projected_savings, ".", sep="")
