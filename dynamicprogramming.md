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

py ```

def KnapSack(capacity,weight,vallue,n):

# ---------- base case ----------
  if n == 0 or capacity == 0:
    return 0
  if (weight[ n - 1] > w):
    return KnapSack(capacity,weight,value, n - 1)
   else:
    return max(
      val[ n - 1] + KnapSack( capacity - weight[ n-1 ], weight, value, n-1 ), KnapSack(capacity, weight, value, n-1)
      
   if __name__ == '__main__':
      profit = [60,100,120]
      wweight = [10,20,30]
      capacity = 50
      n = len(profit)
      print(KnapSack(capacity, weight, profit,n)
      

```

Base Case if n == 0 or capacity == 0: return 0.
if weight of the nth item is more than Knapsack capacity , then the item cannot be include in optimal solution

return maximum of two cases
(1) nth item included
(2) not included
