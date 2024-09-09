m_income = int(input("Enter your monthly income: "))
m_expenses = int(input("Enter your total monthly expenses: "))
m_saving = m_income - m_expenses
y_saving = m_saving * 12
i_saving = y_saving + (y_saving * 0.05)

print(f"Your monthly savings are ${m_saving}.")
print(f"Projected savings after one year, with interest, is: ${i_saving}.")
