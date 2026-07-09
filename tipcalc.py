print("Welcome to the tip calculator!")
total=int(input("What is the bill amount? $"))
tip=int(input("What percentage of tip would you like to pay? 10, 12 or 15? "))
no_of_people=int(input("How many people are splitting the bill? "))

tip_percentage=(12/100)
total+=total*tip_percentage
cost_per_person=total/no_of_people
cost=round(cost_per_person,2)

print("Each person has to pay: $"+ str(cost))