# Check if all items is divisible
# def Greed():
# 	for i in range(n):
# 		if val[i]%wt[i]==0:
# 			return True
def knapsack(n,C,K):
	if C != 0:
		for i in range(n): #i should not depend on for loop rather recursive function
			if vpw[i] == max(vpw):
				if(C-wt[i])>=0: 						#if we can take the whole weight
					K += val[i]
					C -= wt[i]
					print(K,C,"m")
					if len(vpw)!= 1:
						vpw.pop(i)
						#print(vpw[i])
						knapsack(len(vpw),C,K)
				elif (C-wt[i])<=0: 									#if we cant take the whole weight
					K += C*vpw[i]
					C = 0
					print(K,C,"f")
					break;
					
	else:
		print(k,"k")

item =[1,2,3,4]
val =[20,30,50,10]
wt =[2,5,10,5]
vpw = [val/wt for val,wt in zip(val,wt)]  # vpw=val/wt
K = 0                                     # Knapsack Value
n = len(vpw)
C = 16
knapsack(4,C,K)



# if Greed(val,wt):
# 	knapsack(Capacity , weight, val, n,vpw)
