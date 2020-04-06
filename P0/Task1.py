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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
# Get all the phone numbers from texts and calls
# By defining function to count for unique phone numbers


dic = {}
count = 0
for ph1, ph2, time in texts:
    if ph1 not in dic:
        dic[ph1] = count
        count+=1
    if ph2 not in dic:
        dic[ph2] = count
        count+=1

for ph1, ph2, time, duration in calls:
    if ph1 not in dic:
        dic[ph1] = count
        count+=1
    if ph2 not in dic:
        dic[ph2] = count
        count+=1        

print('There are', count, ' different telephone numbers in the records')