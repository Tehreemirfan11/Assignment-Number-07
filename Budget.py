Shopping = ["clothes", "Jewelry", "shoes", "Jacket"]
Quantity= [3, 1, 2, 1]
Price= [1200, 2000, 1000, 1500]
Clothes= 3*1200
Jewelry= 1*2000
shoes= 2*1000
Jacket= 1*1500
Total= (Clothes+Jewelry+shoes+Jacket)
budget = int(input("Enter your budget: "))
if Total<= budget:
    print("You can Buy")
    print("Total cost: ", Total, "Rs")
else:
    print("You Can't Buy")
Remaining= budget - Total
print (f"Remaining Amount: ", Remaining)