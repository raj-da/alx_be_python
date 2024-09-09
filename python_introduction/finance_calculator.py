m_income = float(input("Enter your monthly income: "))
m_expenses = float(input("Enter your total monthly expenses: "))
m_savings = m_income - m_expenses

print(f"Your monthly savings are {m_savings}.")
print(f"projected savings after one year, with interest, is: {m_savings * 12 + (m_savings * 12 * 0.05)}")
