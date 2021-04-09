"""
Author = Francisco Junior
"""

#Input data received
notes = []
sum = 0
average = 0

for x in range(0,4):
    note = float(input("Enter with a you note: "))
    notes.append(note)

print("List of notes is: ",notes)


for i in notes:
    sum += i #sum of notes in list


#Calculating average of notes
average = ((sum) / 4)

#printing of note average
print("Average of notes is: ", average)

