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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

"""
My steps
1. Find numbers starts with (080)
2. parse area codes
3. parse mobile prefixs

"""
# Part A
s = '(080)'
codes = []
count = 0

# Add area codes in array
for ph1, ph2, time, duration in calls:
  if s in ph1:
    if ph2.startswith('('):
      index = ph2.find(')')+1
      codes.append(ph2[0:index])

    elif ph2.startswith('140'):
        codes.append('140')

    else:
         index = ph2.find(' ') 
         codes.append(ph2[0:index-1])

# sort codes
codes.sort()

# print out one per line in lexicographic order with no duplicates
print("The numbers called by people in Bangalore have codes:")
# Find unique codes in array
unique_codes = []
num_calls_in_Banglore = 0
for code in codes:
  if code not in unique_codes:
    # unique_codes.append(code)
    print(code, '\n')
  if code == s:
    num_calls_in_Banglore+=1
    
# Part B: What percentage of calls from fixed lines in Bangalore are made
# to fixed lines also in Bangalore?
percent_calls_within_Banglore = (num_calls_in_Banglore*100)/len(codes)
print(format(percent_calls_within_Banglore, '.2f'), "percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")


