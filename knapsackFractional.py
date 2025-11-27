def knapSack(W, wt, val, n): 
    gain = 0
    
    # Take the ratio of profit and weight array 
    ratio = [0 for i in range(n)] 
    for i in range(n): 
        ratio[i] = val[i] / wt[i] 
    
    # Sort the products of ratio in descending order 
    # for i in range(n): 
    #     for j in range(i + 1, n): 
    #         if ratio[i] < ratio[j]: 
    #             ratio[i], ratio[j] = ratio[j], ratio[i] 
    #             val[i], val[j] = val[j], val[i] 
    #             wt[i], wt[j] = wt[j], wt[i] 
    Zipped_=zip(ratio,val,wt)
    Zipped=sorted(list(Zipped_), reverse=True)
    # Pick items
    for i in range(n):
        if Zipped[i][2]<=W:
            gain+=Zipped[i][1]
            W-=Zipped[i][2]
        else:
            gain+=Zipped[i][1]*(W/Zipped[i][2])
            break
        # if wt[i] <= W: 
        #     gain += val[i] 
        #     W -= wt[i]
        # else: 
        #     gain += val[i] * W / wt[i] 
        #     break
    return gain


profit = [10, 5, 3, 2, 8, 7, 11]
weight = [2, 3, 1, 4, 3, 2, 7]
W = 6
n = 7
print(knapSack(W, weight, profit, n))