"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# Creat sets
Sph1 = set()
S = set()
Outgoing_calls = []

for ph1, ph2, time, duration in calls:
    Sph1.add(ph1)
    S.add(ph2)

for ph1, ph2, time in texts:
    S.add(ph1)
    S.add(ph2) 
    
# set difference gives only out going calls 
Tele_Marketers = Sph1-S
# Convert set to list
Tele_Marketers = list(Tele_Marketers)

# # Print a message:

print("These numbers could be telemarketers: ")
for ph in  sorted(Tele_Marketers):
    print(ph)