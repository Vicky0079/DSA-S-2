# Measuring time
# 1} Measuring time :- 
# import time
# start=time.time()
# for i in range(1,101):
#     print(i)
# print(time.time()-start)
# This code measures the time taken to print numbers from 1 to 100. by for loop take 0.0043sec

# import time
# start=time.time()
# i=1
# while i<=100:
#     print(i)
#     i+=1
# print(time.time()-start)
# This code is intended to print numbers from 1 to 100 using a while loop, take 0.0049sec

# problems with this approach:
# 1)Different time for different algorthm ✔️
# 2)Time varies if implementation changes ❌
# 3)Different machines different time ❌
# 4)Does not work for extremely small inputs ❌
# 5)time varies for different inputs, but can't establish a relationship ❌

# 2} Counting operations :-

# def c_to_f(c): 
#     return (c*9.0/5)+32 #3 operations

# def mysum(x):
#     total = 0 
#     for i in range(x+1): 
#         total += i 
#     return total

# ⚡ Total Operations
# - Initialization = 1
# - Loop body = (x+1)
# - Return = 1
# 👉 Total = (x+1) + 2 operation

#confusion we can't count return as operantion always

# - Initialization (outside loop)
# - total = 0 → 1 operation
# - Inside the loop (per iteration)
# For each i:
# - Loop control → check condition (i < x+1)
# - Increment → move to next i
# - Addition/Assignment → total += i
# - 👉 That’s 3 operations per iteration.
# - Return
# - Sometimes teachers ignore return in operation count (depends on convention).
# - Your teacher’s method → 1 + 3x (init + 3 ops per iteration).

# 1+X #X is input how many time  X run.  if X run 10 then x=10
# T=1+3X

# problems with this approach:
# 1)Different time for different algorthm ✔️
# 2)Time varies if implementation changes ❌
# 3)Different machines different time ✔️
# 4)Does not work for extremely small inputs ❌
# 5)time varies for different inputs, but can't establish a relationship ❌

# Differnt inputs changes how the program runs

# when input is first element in the list -> Best case
# when input is last element in the list -> Worst case
# when input is somewhere in the middle -> Average case

# when we desgin algorithm we desgine for worst case scenario

#3} order of growth :-
#goals:
#1.want to evaulate program efficency when input is very large
#2.want to express the growth of program run time as input size grows in short we want a graph between time and input size
#3.we basicallly take worst case scenario
#4.we not want exact relaionshiop between time and input size we only want general trend
    # like T=i^2+2i+3 we only want i^2 that tell only quadratic relation between time and input size
    # like T=3i+4 we only want i that tell linear relation between time and input size
#5.we will look at largest factors in run time 
   #like we write 
     # single for loop
       # for loop.......   #n
     # nested for loop
       # for loop......... #n^2
         # for loop.......
 #since nested loop is more significant we will look at nested loop only becouse it take more time


# Big O notation :-
# O() 
#Exact steps vs O()
# def fact_iter(n):
#     answer = 1                     # 1 operation
#     while n > 1:                  # 1 operations
#         answer *= n                # 2 operation
#         n -= 1                     # 2 operation
#     return answer                  
# # Total operations = 1+5n  , where n is the input number. that the exact steps
# Now in o()
#  we remove constant and non dominant terms
# so here we remove 1 and we take 5n so we have O(5n)
# and we remove constant so we have O(n) 
# it mean linear relationship between time and input size

#so the idea is simple
#1. n^2+2n+2  
#        now we see here n^2 which mean here is nested loop so we take n^2
#        now we see n which mean loop is run
#        now we see 2 which is with n tell two opperations in loop
#        now we see single 2 which out off all loop 2 opertions

# now we tell big o notation 
# n^2 is dominant term so we take n^2
# so we have O(n^2)
#   Time complexity of this program is O(n^2)
#     here relationship between time and input size is quadratic

#2. n^2+100000n+3^1000
# here n^2 is dominant term so we take n^2
# so we have O(n^2)
#   Time complexity of this program is O(n^2)

#3. log(n)+n+4
# here n is dominant term so we take n
# so we have O(n)
#   Time complexity of this program is O(n)

#4. 0.0001*n*log(n)+300n
# here n is dominant term so we take nlog(n)
# so we have O(nlog(n))
#   Time complexity of this program is O(nlog(n))

#5. 2n^30 +3^n
# here 3^n is dominant term so we take 3^n
# so we have O(3^n)
#   Time complexity of this program is O(3^n)


