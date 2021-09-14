
Algorithm exists(A, n, x):
    lo = 0
hi = n-1
while hi >= lo:
        mid = floor((hi+lo)/2)
        if x > A[mid]:
            lo = mid+1
        else if x < A[mid]:
         hi = mid-1 else:
            return True
return False

####################################################
Del 1)
####################################################

Antag at A = [1,5,6,10,12,16,17,43]. 
Dvs:
A[0] = 1,A[1] = 5,...,A[7] = 43.

#####################################
(a) Hvad returnerer exists(A, 8, 6)?
#####################################
lo = 0 
hi = 7 
while 7 ≥ 0 
     mid = floor((7+0)/2) -> 3  (da der rundes ned når der står floor)

     if 6 > A[3]-> 10 - condition is false 
    else if 6 < 10:
    hi = 2

lo = 0 
hi = 2
while 2 ≥ 0 
    mid = floor((2+0)/2) = 1
    if 6 > A[1] - condition is true
    lo = 2

lo = 2
hi = 2
while 2 ≥ 2
    mid = floor((2+2)/2) = 2
    if 6 > A[2] - condition is false
    else if 6 < A[2] - condition is false 
    
    -> return true 

######################################
(b) Hvad returnerer exists (A,8,13)
######################################
lo = 0
hi = 7 
while 7 ≥ 0
     mid = ((7+0)/2) = 3 
     if 13 > A[3]:
         lo = 4

lo = 4 
hi = 7 
while 7 ≥ 4
      mid = ((7+4)/2) = 5
      if 13 > A[5] - condition is false 
      else if 13 < A[5]
          hi = 4

lo = 4 
hi = 4
while 4 ≥ 4 
     mid = ((4+4)/2) = 4
     if 13 > A[4] - condition is true
         lo = 5

lo = 5
hi = 4 
while 4 ≥ 5 - condition is false -> return false 
     


######################################
(c) Hvad returnerer exists (A,5,16)
######################################
lo = 0 
hi = 4 
    while 4 ≥ 0 
        mid = ((4+0)/2) = 2 
        if 16 > 6:
            lo = 3

lo = 3
hi = 4 
    while 4 ≥ 3 
        mid = ((4+3)/2) = 3 
        if 16 > A[3]
            lo = 4 

lo = 4 
hi = 4 
    while 4 ≥ 4 
        mid = ((4+4)/2) = 4
        if 16 > A[4]
            lo = 5 
lo = 5
hi = 4
while 4 ≥ 5 condition is false -> return false 

#####################################

(d) iteration 1 2 3
           lo 4 4 5
          mid 3 5 4
           hi 7 4 4 

#####################################

#####################################################################
Del 2) Forklar med jeres egne ord, hvad funktionen exists gør.
#####################################################################

- Funktionen exists tjekker om x er en del af arrayet 

######################################################################
Del 3) Antag nu at tallene A[0], . . . , A[n − 1] ikke er sorterede.
######################################################################

