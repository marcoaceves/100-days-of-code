# tip calculator

bill = input("What is the total?")
people =input ("How many people in your group?")
tip =input ("how much '%' would you like to tip?")

bill = int(bill)
people = int(people)
tip = int(tip) / 100

output = bill * tip / people

print('$'+ str(output) +' tip per person')
pass