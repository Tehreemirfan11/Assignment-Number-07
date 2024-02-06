#Time in Minutes 
Clean_your_Workspace= 10
Reading_One_Chapter= 120
Daily_Exercise= 60
Arrange_your_Shelf= 30
Clean = int(input("Time that you spend on clean your workspace: "))
Reading = int(input("Time that you Spend on Reading one Chapter: "))
Exercise = int(input("Your Exercise Time: "))
Shelf= int(input("Time that you spend on Arranging your Shelf: "))
if Clean_your_Workspace == Clean:
    print("you are Perfect in Cleaning")
elif Clean_your_Workspace < Clean:
    print("You Have to Improve in Cleaning")
else:
    print("Wow! you are too Fast in Cleaning")
if Reading_One_Chapter== Reading:
    print("Perfect in Reading")
elif Reading_One_Chapter < Reading:
    print("You Have to Improve your Reading")
else:
    print("Wow! you are too Fast in Reading") 
if Daily_Exercise== Exercise:
    print("You spend Perfect Time on Exercise")
elif Daily_Exercise < Exercise:
    print("You Spend too much time on Exercise")
else:
    print("You Spend very Less time on Exercise")
if Arrange_your_Shelf == Shelf:
    print("You are Perfect in arranging your Shelf")
elif Arrange_your_Shelf < Shelf:
    print("You are Slow in Arranging your Shelf")
else:
    print("Wow! you are too Fast in Arranging your Shelf")                        