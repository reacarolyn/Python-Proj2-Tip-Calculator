# Welcome to my tip calculator project

#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00/5) * 1.12
#Round the result to 2 decimal places
150
print("Welcome to the tip calculator.")
totalBill = float(input("What is the total bill? "))
tipPercent = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
numPerson = int(input("How many people to split the bill? "))
tip = tipPercent/100 + 1
eachPerson = (totalBill/numPerson)* tip
final_amount = round(eachPerson,2)
final_amount = "{:.2f}".format(eachPerson)
print(f"Each person should pay: ${final_amount}")

