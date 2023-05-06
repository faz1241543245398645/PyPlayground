simplify decision by breaking down problem into sub-problem (related with Devide and Conquer)

the solution of sub-problem will be stored and used for another related sub-problem.

This array of solution make the decision optimized.

Knap Sack Problem.

to know capacity of weight, and the table of values stated item list together with its wight and values 

| i  |   |   |   |   |
|---|---|---|---|---|
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |

```

def knapsack(W, wt, val, n):
    # Initialize a 2D array to store the maximum value of items that can be picked up
    # for every weight from 0 to W and for every item from 0 to n
    # we need to store the values for all possible combinations of weights and items, including 0 weight and 0 item thats why we increment the size of the element by 1
    K = [[0 for x in range(W+1)] for x in range(n+1)]
 
    # Build table K[][] in bottom-up manner
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0: #basecase , notice there are or there. means if the weight is still bigger than capacity given it will go to the basecase
                #but we dont increase the capacity ,we just increase the i so that it can iterate bigger set of array each time
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
            print(K[i][w],"K[",i,"][",w,"]") #notice that the w is always 5, its because the w have finished iterate until 5
        #for loop should iterate until 6 right? because the w is 5 + 1
        # yes its 5 + 1 but the element is [0,1,2,3,4,5]
 
    return K[n][W]


Item = [1,2,3,4,5]
Weight = [3,1,1,2,2]
Value = [13,12,10,17,15]

n = len(Item)
W = 6

print(knapsack(W, Weight, Value, n))
      
  ```


Base Case if n == 0 or capacity == 0: return 0.
if weight of the nth item is more than Knapsack capacity , then the item cannot be include in optimal solution

return maximum of two cases
(1) nth item included
(2) not included
