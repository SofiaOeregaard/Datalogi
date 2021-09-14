
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
    7 = 2 - condition is false
    
    return true 

######################################
(b) Hvad returnerer exists (A,8,13)
######################################
lo = 0
hi = 7 
while 7 ≥ 0
     mid = ((7+0)/2) = 3 
     if 13 > 10:
         lo = 4

#tjekker: 7 ≥ 4 -> condition er stadig sand så while loop kører igen 

lo = 4 
hi = 7 
while 7 ≥ 4
      mid = ((7+4)/2) = 5
      if 13 > 16:
          lo = 6
#tjekker: 7 ≥¸6 -> condition er stadig sand så while loop kører igen 

lo = 6 
hi = 7 
while 7 ≥ 6 
     mid = ((7+6)/2) = 6
     if 13 > 17
         lo = 7 
#tjekker: 7 ≥ 7 -> condition er stadig sand så loop kører igen 

lo = 7 
hi = 7 
while 7 ≥ 7 
     mid = ((7+7)/2) = 7 
     if 13 > 43 - condition is false 
     else if 13 < 43:
        hi = 6 
#tjekker: 6 ≥ 7 -> condition er false 
return false 


######################################
(c) Hvad returnerer exists (A,5,16)
######################################
lo = 0 
hi = 4 
    while 4 ≥ 0 
        mid = ((4+0)/2) = 2 
        if 16 > 6:
            lo = 3 
#tjekker: 4 ≥ 3 -> condition er sand, while loop fortsætter 

lo = 3
hi = 4 
    while 4 ≥ 3 
        mid = ((4+3)/2) = 3 
        if 16 > 10 
            lo = 4 
#tjekker: 4 ≥ 4 -> condition er sand, while loop fortsætter

lo = 4 
hi = 4 
    while 4 ≥ 4 
        mid = ((4+4)/2) = 4
        if 16 > 12
            lo = 5 
#tjekker 4 ≥ 5 - condition er false 
return false  

#####################################
(d) 
#####################################

#####################################################################
Del 2) Forklar med jeres egne ord, hvad funktionen exists gør.
#####################################################################

- Funktionen exists tjekker om x er en del af arrayet 

######################################################################
Del 3) Antag nu at tallene A[0], . . . , A[n − 1] ikke er sorterede.
######################################################################

