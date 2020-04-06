"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
duration_Max= 0
dic = {}
for ph1, ph2, time, duration in calls:
    if ph1 in dic:
        dic[ph1]+=duration
    elif ph1 not in dic:
        dic[ph1] = duration

    if ph2 in dic:
        dic[ph2]+=duration    
    elif ph2 not in dic:
        dic[ph2] = duration    
ph1_Max= max(dic)
duration_Max = dic[max(dic)]
print(ph1_Max, 'spent the longest time,', duration_Max, "seconds, on the phone during September 2016.")        