Width= int(input("Width of Steel Bar in millimeters: "))
perchase= int(input("How many Kg you perchase this Month? "))
Sell= int(input("How many Kg you Sold this month? "))
Utilities= int(input("Electricity Bil per month: "))
Salary= int(input("Employees Salaries per month: "))
Transport= int(input("Cost of Transportation per month: "))
if Width == 2:
    perchasing_price = 175
    selling_price = 180
    perchasing_price*=perchase
    selling_price*=Sell
    profit = perchasing_price - selling_price
    Total=(Utilities+Salary+Transport)
    profit -= Total
    print(f"Your Profit is of This Month is: {profit}")
elif Width == 3:
    perchasing_price = 180
    selling_price = 185
    perchasing_price*=perchase
    selling_price*=Sell
    profit = perchasing_price - selling_price
    Total=(Utilities+Salary+Transport)
    profit -= Total
    print(f"Your Profit is of This Month is: {profit}")
elif Width == 4:
    perchasing_price = 185
    selling_price = 190
    perchasing_price*=perchase
    selling_price*=Sell
    profit = perchasing_price - selling_price
    Total=(Utilities+Salary+Transport)
    profit -= Total
    print(f"Your Profit is of This Month is: {profit}")
    
else:
    print("Sorry! This width is not available: ")