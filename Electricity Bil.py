#Electricity Bil Calculator
Rs_of_one_Unit= 24.7
tax_on_one_Unit= 3.3
Units= float(input("Number of Units used per Month: "))
Total_Tax= Units*tax_on_one_Unit
Units_Cost= Units*Rs_of_one_Unit
Total_Cost= Total_Tax + Units_Cost
print(f"Bil without Tax: {Units_Cost}")
print(f"Tax: {Total_Tax}")
print(f"Your Total Electricity Bil is: {Total_Cost} Rupees")