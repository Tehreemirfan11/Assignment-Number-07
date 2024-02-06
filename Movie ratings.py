Genre= input ("Enter Genre: ")
Movie_Name= ()
Ratings= ()
Release_Year=()
if Genre=="Comedy":
    Movie_Name = "The Wolf of Wall Street"
    Ratings= 4.5
    Release_Year= 2013
    print(f"Name of Movie: {Movie_Name}")
    print(f"Ratings of This Movie: {Ratings}")
    print(f"This Movie is Release in: {Release_Year}")
elif Genre =="Action":
    Movie_Name= "The Creator"
    Ratings= 3.6
    Release_Year= 2023
    print(f"Name of Movie: {Movie_Name}")
    print(f"Ratings of This Movie: {Ratings}")
    print(f"This Movie is Release in: {Release_Year}")
elif Genre== "Horror":
    Movie_Name= "A Haunting in Venice"
    Ratings= 3.0
    Release_Year= 2023
    print(f"Name of Movie: {Movie_Name}")
    print(f"Ratings of This Movie: {Ratings}")
    print(f"This Movie is Release in: {Release_Year}")
elif Genre == "Adventure":
    Movie_Name= "Teefa in Trouble"
    Ratings= 4.7
    Release_Year= 2018
    print(f"Name of Movie: {Movie_Name}")
    print(f"Ratings of This Movie: {Ratings}")
    print(f"This Movie is Release in: {Release_Year}")
else:
    print("Not Available") 