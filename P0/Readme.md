# Calculate Big O:

## Task0: 
**List is represented as array.**
Time required to access any elemnt in array is O(1). Means constat time to get first record of texts or last record of calls. 

Worst-Case Big-O = O(1)

## Task1:
Iterator have O(n) time complexity where n is number of elements in the list.
Two seprate for loops are used to get total count of unique phone numbers from record.
Each for loop goes through 7 instructions.

Worst-Case Big-O = 7*O(n) + 7*O(n) = 14*O(n)

## Task2:
As explained above, time complexity for signle for loop is O(n) to find phone number who spent longest time duration.
This loop goes through 4 instructions.

Worst-Case Big-O = 4*O(n)

## Task3:
To get codes from calls list, one for loop is used which iterate over len(calls).
This loop goes through maximum 4 instructions in worst case.


```
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
```

But later in code used sort() to get codes in lexicographic order. Whose time complexity is.

Worst-Case Big-O = O(nlogn)

**Note:** I don't see how time complexity is O(n2) as mentioned in previous feedback. As I am using only one for loop and not a nested loop.

## Task4:
To access all phone numbers from texts list, for loop need to go through 9072 rows.
Set difference is used, to access out going calls, as explained in previous feedback time complexity of set function is O(constant).
At the end sort() method is used on 43 phone numbers, to print telemarkater phone numbers in lexicographic order.
Whose time complexity is O(nlogn) = 233.49.

Worst-Case Big-O = O(nlogn)


