daily_steps = [int(step) for step in input("Daily Steps: ").split(',')]
distance_walked = [float(Distance) for Distance in input("Distance in meters : ").split(',')]
calories= [int(cal) for cal in input("Calories: ").split(',')]
average_steps= sum(daily_steps) / len(daily_steps)
total_distance_per_month = sum(distance_walked) * 30
print("Average steps: " ,average_steps)
print("Total distance in month: ",total_distance_per_month)