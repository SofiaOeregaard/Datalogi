Øvelsesopgaver mandag 13/9-2021

Opgave CLRS 2.1-1)
for j = 2 to A.length
    key = A[j]
    i = j - 1

#insert A[j] into the sorted sequence...

    while i > 0 and A[i] > key
        A[i + 1] = A[i]
        i = i - 1
    
    A[i + 1] = key

A = [31,41,59,26,41,58]
key = A[2] -> 41
i = 2 - 1 -> i = 1
1 > 0 and 31 > 41 - condition 
A[1+1]= key -> A[2] = 41

key = A[3] -> 59
i = 2
2 > 0 and 41 > 59 - condition 
A[3] = 59 

key = A[4] -> 26 (KEY!)
i = 3 
3 > 0 and 59 > 26 - true 
A[4] = 59 
i = 2

kører while loop igen (while loop går mod venstre):
A[2] -> 41
i = 1
sammenligner: 1 > 0 and 41 < 26 - true 

kører while loop igen
A[1] -> 31
i = 0 
sammenlinger: 0 > 0 and 31 < 26 - condition 
A[1] = 26

nyt array: A[26,31,41,59,41,58]

Tilbage til for loop:
key = A[5] -> 41
i = 4

4 > 0 and 59 > 41 - true
A[5] = 59
i = 4 

nyt array: A[26,31,41,41,59,58]

kører while loop igen:
A[5] = 59
i = 3

sammenlinger: 3 > 0 and 41 > 41 - condition 

Tilbage til for loop:
A[6] -> 58 
i = 5 
sammenligner: 5 > 0 and 59 > 58 - true 

while loop:
    A[6] = 59 
    i = 5 

nyt array: A[26,31,41,41,58,59]

sammenlinger: 5 > 0 and 41 > 59 - condition 

A[6] = 59 

-> A = [26,31,41,41,58,59]
 

