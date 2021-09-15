CLRS 2.1-2.

Rewrite the Insertion-Sort procedure to sort into nonincreasing instead of nondecreasing order

The Insertion-Sort:
for j = 2 to A.length
    key = A[j]
    i = j - 1

#insert A[j] into the sorted sequence...

    while i > 0 and A[i] > key
        A[i + 1] = A[i]
        i = i - 1
    
    A[i + 1] = key



A = [31,41,59,26,41,58]
